import streamlit as st
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config
import pandas as pd
import base64

def parse_lantents(latent, Gs):
    parsed_latent_vect = None  # Latent vector parse is none by default
     # Try to parse latent vector string
    try:
        parsed_latent_vect = [float(item) for item in latent.split(" ")]
        
        if(len(parsed_latent_vect) == 1):
            # Extend value to match size
            parsed_latent_vect = list(parsed_latent_vect) * int(Gs.input_shape[1])
        elif (len(parsed_latent_vect) < int(Gs.input_shape[1])):
            # Fill remaining values with zeros.
            zeros = [0] * (int(Gs.input_shape[1]) - len(parsed_latent_vect))
            parsed_latent_vect.extend(zeros)
        else:
            # Take first 512 values
            parsed_latent_vect = parsed_latent_vect[:int(Gs.input_shape[1])]
    
        parsed_latent_vect = np.array([parsed_latent_vect], dtype = float)
    # If latent vector parsing fails (due to invalid value in list)
    except ValueError as e:
        st.write('Invalid value in list for latent vector. Using random latent vector instead.')
        latent_vect = None

    return parsed_latent_vect

def generate_random_figures(number_figures, trunc_psi, trunc_cutoff, latent_vect, rand_inputs, trunc_trick, Gs):
    imgs = []                  # Initiate empty image list
    parsed_latent_vect = None  # Latent vector parse is none by default
    latents_used = []

    # Disable truncation trick in case the user select to
    if trunc_trick == False:
        trunc_psi = None
        trunc_cutoff = None

    # Parse Latent Vector
    latent_vect = parse_lantents(latent_vect, Gs)
    
    # For each image solicited by user
    for i in range(0,number_figures):
        rnd = np.random.RandomState(None)

        # Check if latent vector isn't defined
        if(latent_vect is None):
            # Fill with random latent vector
             latents = rnd.randn(1, Gs.input_shape[1])
            
        else:
            latents = latent_vect

        # Generate image.
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        images = Gs.run(
            latents, 
            None, 
            truncation_psi=trunc_psi, 
            truncation_cutoff = trunc_cutoff, 
            randomize_noise=rand_inputs, 
            output_transform=fmt)

        imgs.append(PIL.Image.fromarray(images[0], 'RGB'))
        latents_used.append(latents[0].tolist())
        
    return imgs, latents_used

#@st.cache(hash_funcs={dnnlib.tflib.network.Network: lambda _: None},suppress_st_warning=True)
def init():

    tflib.init_tf()

    #Gs = pickle.load(open("/content/Collab/results/image_generation.pkl", "rb"))
    Gs = pickle.load(open("results/image_generation.pkl", "rb"))

    return Gs

def get_table_download_link_csv(df):
    #csv = df.to_csv(index=False)
    csv = df.to_csv(header=False, index=False, sep=" ").encode()
    #b64 = base64.b64encode(csv.encode()).decode() 
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="latent_vectors.csv" target="_blank">Download latent vectors as CSV file</a>'
    return href


def generate_single_image(Gs, latent):
    rnd = np.random.RandomState(None)

    # Check if latent vector isn't defined
    if(latent is None):
        # Fill with random latent vector
        latents = rnd.randn(1, Gs.input_shape[1])
    else:
        latents = latent
    # Generate image.
    fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
    images = Gs.run(
        latents, 
        None, 
        randomize_noise=False, 
        output_transform=fmt)

    return latents, PIL.Image.fromarray(images[0], 'RGB')

def generate_images_animation(Gs, latents_initial_image, latents_final_image, steps, trunc_psi, trunc_cutoff, trunc_trick):
    # List used to accumulate the generated images.
    imgs = []       # Image as PIL Object
    img_array = []  # Image as NumPy Array
    anim_latents = [] # Latent vectors used for animation

    transition_latent = latents_initial_image.copy()

    # Disable truncation trick in case the user select to
    if trunc_trick == False:
        trunc_psi = None
        trunc_cutoff = None

    # Mahattan distance between transition latent vector (which is equivalent to initial latent vector) and final latent vector
    st.write("Initial manhattan distance:", np.sum(np.abs(latents_initial_image - latents_final_image)))

    # Producing the intermediary images
    for i in range(0,steps + 2):
        # Producing images for current step
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        anim_latents.append(transition_latent[0].copy())

        images = Gs.run(transition_latent,
            None,
            truncation_psi=trunc_psi, 
            truncation_cutoff = trunc_cutoff, 
            randomize_noise=False, 
            output_transform=fmt)
        
        # Pushing image to end of imgs list.
        imgs.append(PIL.Image.fromarray(images[0], 'RGB'))
        img_array.append(images[0])

        # Incrementing values in latent vector for next step
        if(i < steps + 1):
            transition_latent += ((latents_final_image - latents_initial_image)/steps)
        else:
            transition_latent = latents_final_image.copy()
    

    # Mahattan distance between transition latent vector (which should be very close to the final latent vector) and final latent vector
    st.write("Final manhattan distance:", np.sum(np.abs(transition_latent - latents_final_image)))

    imgs[0].save('transition.gif', save_all=True, append_images=imgs, loop = 0)

    return imgs, img_array, anim_latents

def local_gif():
    """### gif from local file"""
    file_ = open("transition.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
    

def app():
    st.title('StyleWood: User GUI')

    st.header("Image Generation")
    st.write("In this page, you can configure the parameters to use the model we have created to generate images. You can customize the parameters however you want. If the images stop rendering, you can choose to wait a sixty seconds (since too many requests have been made and we're using a free tunneling service, we have to wait to make more) or you can try restarting the web application. ")

    Gs = init()

    # List of parameters
    with st.form('Image Creation Parameters'):
        trunc_psi = st.slider(
            'Truncation PSI',
            min_value = 0.00,
            max_value = 1.00,
            value = 0.70,
            help='Style strength multiplier for the truncation trick. Generally between 0 and 1.'
            )

        trunc_cutoff = st.slider(
            'Truncation Cutoff',
            min_value = 0,
            max_value = 20,
            value = 8,
            help='Number of layers for which to apply the truncation trick.'
            )
        

        number_img = st.slider(
            'Number of Images',
            min_value = 1,
            max_value = 30,
            value = 1,
            help = 'Number of images to produce. It\'s faster to use this to produce multiple images than running the form multiple times.'
            )

        latent_vect = st.text_area(
            'Latent Vector', 
            value='', 
            help='List of floating-point values to use for latent vector. Values should use dots as decimal separators, and spaces to separate values. If a single value is given, that value is used for the 512 positions of the latent vector; If multiple values are given, the first 512 are used for the latent vector; If less than 512 values are given, the rest are filled with zeros; If no values are given, then a random latent vector is generated.'
        )

        # Separate click boxes into three colums
        colA, colB, colC = st.beta_columns([1,1,1])

        with colA:
            rand_inputs = st.checkbox(
                'Randomize Inputs', 
                value=False, 
                help='Randomize inputs for model. When this is true, the same latent vector can generate a different image.'
        )

        with colB:
            trunc_trick = st.checkbox(
                'Truncation Trick', 
                value=True, 
                help='When enabled, should improve image quality.'
            )
        with colC:
            view_vectors = st.checkbox(
                'Show Vectors', 
                value=True, 
                help='After all the images have been rendered, output a list containing all the latent vectors that were used.'
            )

        submit_button =  st.form_submit_button(label='Generate New Images')

    figures, latents = generate_random_figures(number_img, trunc_psi,trunc_cutoff, latent_vect, rand_inputs,trunc_trick, Gs)

    col1, col2, col3 = st.beta_columns([1,6,1])
    # Center images
    with col1:
        st.write("")

    with col2:
        st.image(figures, width=512)

    with col3:
        st.write("")

    
    if view_vectors:
        latents = pd.DataFrame(latents)
        st.dataframe(latents)
        st.markdown(get_table_download_link_csv(latents), unsafe_allow_html=True)


    # Image transition sector
    st.header("Image Transition")
    st.write("In this section, to generate images, the model parameters can be adjusted as needed. You can create and save images, as well as download their latent vector values. If the images stop rendering, you can choose to wait sixty seconds. This usually happens when too many requests have been made. If waiting doesn\'t solve the problem, then restarting the web application may work.")
    
    # Parameters for image transition.
    with st.form('Transition Parameters'):
        enable_transition = st.checkbox(
            'Enable Transitions',
            value = False,
            help = 'If this selection box is disabled, image transitions won\'t be generated. We leave this off by default since generating transitions between images can be a heavy task.'
        )
        latent_vect_a = st.text_area(
            'Latent Vector (Initial Image)', 
            value='', 
            help='List of floating-point values to use for latent vector. Values should use dots as decimal separators, and spaces to separate values. If a single value is given, that value is used for the 512 positions of the latent vector; If multiple values are given, the first 512 are used for the latent vector; If less than 512 values are given, the rest are filled with zeros; If no values are given, then a random latent vector is generated.'
        )

        latent_vect_b = st.text_area(
            'Latent Vector (Final Image)', 
            value='', 
            help='List of floating-point values to use for latent vector. Values should use dots as decimal separators, and spaces to separate values. If a single value is given, that value is used for the 512 positions of the latent vector; If multiple values are given, the first 512 are used for the latent vector; If less than 512 values are given, the rest are filled with zeros; If no values are given, then a random latent vector is generated.'
        )

        steps = st.slider(
            'Number Of Steps', min_value=5, max_value=500, value=100, step=1,help='Number of intermidiary images to produce for the transition/animation. Larger values generate larger and longer GIFs.',
        )

        submit_button =  st.form_submit_button(label='Generate New Transition')

    # If it has been selected to allow transitions (by default we turn it off, since it's a heavy operation)
    if(enable_transition):
        colx, coly, colz = st.beta_columns([1,6,1])

        with colx:
            st.write("")

        # Centralized column containing Initial image, final image and transition gif
        with coly:
            
            st.header('Initial Image')
            lv_a = parse_lantents(latent_vect_a, Gs)
            lv_a, img_a = generate_single_image(Gs,lv_a)
            st.image(img_a, width=512)

            st.header('Final Image')
            lv_b = parse_lantents(latent_vect_b, Gs)
            lv_b, img_b = generate_single_image(Gs,lv_b)
            st.image(img_b, width=512)

            st.header('Transition')
            imgs, img_array, anim_latents = generate_images_animation(Gs=Gs,latents_initial_image=lv_a, latents_final_image=lv_b, steps=steps, trunc_psi=trunc_psi, trunc_cutoff=trunc_cutoff, trunc_trick=trunc_trick)

            local_gif()

        with colz:
            st.write("")

        st.write("")

        # Display Latent Vectors
        if view_vectors:
                    anim_latents = pd.DataFrame(anim_latents)
                    st.dataframe(anim_latents)
                    st.markdown(get_table_download_link_csv(anim_latents), unsafe_allow_html=True)