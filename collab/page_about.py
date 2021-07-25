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

    st.write("Information for this section has been removed for blind peer review process.")

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

    