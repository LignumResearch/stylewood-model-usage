import streamlit as st

def app():
    st.title("About Us")

    st.write("This web application was created to enable users to experiment with the model created in the paper entitled ... (removed for blind peer review process) by ... (removed for blind peer review process)")

    st.markdown(
        """
        The full paper can be found at: [link text](https://). 

        The Github Repository containing the model and the code for this project can be found at: [https://github.com/LignumResearch/stylewood-model-usage](https://github.com/LignumResearch/stylewood-model-usage).
        """
    )

    # Authors Section
    st.header("Authors")

    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=1xIHH07F2HDNqq9DHWn80BIYHyV09P44d')
    with col2:
        st.markdown(
        """
        **Dercilio Junior Verly Lopes**: 
        Department of Sustainable Bioproducts (DSB)/Forest and Wildlife Research Center (FWRC), Mississippi State University, Mississippi State, MS, 39762-9820, USA.
        - [Email](mailto:dvl23@msstate.edu)
        - [LinkedIn](https://www.linkedin.com/in/dvl23msu/)        
         """
        )
    
    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=12dwWoE6DEPvcIVlE2Rlq3hiVW7yDjpVE')
    with col2:
        st.markdown(
        """
        **Gustavo Fardin Monti**: 
        Universidade Federal do Espírito Santo (UFES). Centro Universitario do Norte do Espírito Santo (CEUNES). Curso de Bacharelado em Engenharia da Computação. São Mateus, ES - Brazil.
        - [Email](mailto:gustavo_m@hotmail.co.uk)
        - [LinkedIn](https://www.linkedin.com/in/gustavo-fardin-monti/)        
         """
        )

    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=1Js0s04Xfh5Yg2huZS80q_Q0mpcdyCwSw')
    with col2:
        st.markdown(
        """
        **Greg W. Burgreen**: 
        Center for Advanced Vehicular Systems (CAVS), Mississippi State University, Starkville, MS 39759, USA.
        - [Email](mailto:greg.burgreen@msstate.edu)
        - [LinkedIn](https://www.linkedin.com/in/greg-burgreen-1150948/)        
         """
        )
    
    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=1J4Wql2-nyyK7uqHnZ7oqdJLw-qKyFb_V', width = 163)
    with col2:
        st.markdown(
        """
        **Jordão Cabral Moulin**: 
        Departamento de Ciências Florestais e da Madeira, Universidade Federal do Espírito Santo (UFES), Jerônimo Monteiro, ES - Brazil.
        - [Email](mailto:jordao_cm@hotmail.com)
        - [LinkedIn](https://www.linkedin.com/in/jord%C3%A3o-cabral-moulin-60751732/)        
         """
        )

    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=1IaGScgSnhPGUjAdeZbIAtuENO7hTfs5o')
    with col2:
        st.markdown(
        """
        **Gabrielly dos Santos Bobadilha**: 
        Department of Sustainable Bioproducts (DSB)/Forest and Wildlife Research Center (FWRC), Mississippi State University, Mississippi State, MS, 39762-9820, USA.
        - [Email](mailto:gd450@msstate.edu)
        - [LinkedIn](https://www.linkedin.com/in/gabrielly-bobadilha-069ab7103/)        
         """
        )

    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=14H2p9g-pc_hj_Ix47HfDcCtYcze9LTQS')
    with col2:
        st.markdown(
        """
        **Edward D. Entsminger**: 
        Department of Sustainable Bioproducts (DSB)/Forest and Wildlife Research Center (FWRC), Mississippi State University, Mississippi State, MS, 39762-9820, USA.
        - [Email](mailto:Edward.entsminger@msstate.edu)
        - [LinkedIn](https://www.linkedin.com/in/edward-d-entsminger-m-s-awb%C2%AE-wpit-fp-a-973b2010b/)        
         """
        )
    
    col1, col2 = st.beta_columns([1,3])
    with col1:
        st.image('https://drive.google.com/uc?id=1gTQcrcywXqot3_VqxPJ34ksY-z2SQiV-')
    with col2:
        st.markdown(
        """
        **Ramon Ferreira Oliveira**: 
        Department of Sustainable Bioproducts (DSB)/Forest and Wildlife Research Center (FWRC), Mississippi State University, Mississippi State, MS, 39762-9820, USA.
        - [Email](mailto:rfo17@msstate.edu@msstate.edu)
        - [LinkedIn](https://www.linkedin.com/in/oliveiraeim/)        
         """
        )


    # Credits and References
    st.header("Credits and References")

    st.markdown(
        """
        For the paper, we trained StyleGAN to generate synthetic microscopic cross sections of hardwood species. 

        > A Style-Based Generator Architecture for Generative Adversarial Networks. Tero Karras (NVIDIA), Samuli Laine (NVIDIA), Timo Aila (NVIDIA). [https://arxiv.org/abs/1812.04948](https://arxiv.org/abs/1812.04948). [StyleGAN — Official TensorFlow Implementation](https://github.com/NVlabs/stylegan).

        To train StyleGAN, we used a dataset containing identified microscopic cross-sectional images of hardwoods species by the XDD research team.

        > SUGIYAMA, Junji, HWANG, Sung Wook, ZHAI, ShengCheng, KOBAYASHI, Kayoko, KANAI, Izumi, KANAI, Keiko. [Xylarium Digital Database for Wood Information Science and Education](http://hdl.handle.net/2433/250016).
        
        The complete set of references can be found in our paper. 
        """
    )

    
