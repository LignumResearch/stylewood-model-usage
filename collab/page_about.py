import streamlit as st

def app():
    st.title("About Us")

    st.write("This web application was created to enable users to experiment with the model created in the paper entitled by Lopes D. J. V., Monti G. F., Burgreen, G. W., Moulin J. C., Bobadilha G. S., Entsminger E. D., and Oliveira R. F.")

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
        st.image('https://media-exp3.licdn.com/dms/image/C4D03AQFHgl_TiIvDvg/profile-displayphoto-shrink_800_800/0/1620938294540?e=1631145600&v=beta&t=ijFKWB-HrWl93KElmwVr8P_bJiFZxCHe-iz9JZhHrVc')
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
        st.image('https://media-exp3.licdn.com/dms/image/C4D03AQFwhTcq7IsO5g/profile-displayphoto-shrink_200_200/0/1594251143612?e=1631145600&v=beta&t=wn-6SduOFzsgclv4iqLxsEz17kKXEjIygqWiTZKB328')
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
        st.image('https://media-exp3.licdn.com/dms/image/C4E03AQHHaIwbV3pfFg/profile-displayphoto-shrink_800_800/0/1543086430509?e=1631145600&v=beta&t=175g49R1irHRqpjUOdP9z7ld94JMvd9ZiFV8l-uPMGk')
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
        st.image('https://media-exp3.licdn.com/dms/image/C5603AQEiO92Z5T3tug/profile-displayphoto-shrink_800_800/0/1516505407180?e=1631145600&v=beta&t=KizFxyRrgkFtR5iXP69otoA25MWb3KOSMllsAkrXrXM', width = 163)
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
        st.image('https://media-exp3.licdn.com/dms/image/C4D03AQFELkuNR90rTg/profile-displayphoto-shrink_800_800/0/1587489521804?e=1631145600&v=beta&t=2PU-wcszMWkxgVdxY7GF55oiy4shqIbmLb2jnjDU77E')
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
        st.image('https://media-exp3.licdn.com/dms/image/C4D03AQEi9X1Hu2nJtA/profile-displayphoto-shrink_800_800/0/1599230489599?e=1631145600&v=beta&t=7NWyiTF19Ggux_5UIZU4CXZXa1FYIkBTT3R-mMISH8I')
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
        st.image('https://media-exp3.licdn.com/dms/image/C4E03AQGRvgaO1uAvWg/profile-displayphoto-shrink_800_800/0/1584495178268?e=1631145600&v=beta&t=nE36nGTUfjWeDH3uMBe1PcZHL785K8XkoF7zFFxrv2k')
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

    