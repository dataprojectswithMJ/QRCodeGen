import streamlit as st
import qrcode
import random
from qrtools import QR

st.set_page_config(page_title='QRCode Generator',
                   page_icon=':closed_lock_with_key:')


def main():
    st.image('QRcode_Gen.png')
    st.title("")

    st.header('About this project:')

    st.markdown("This is a open source web application to make generating QR codes much easier. Built using Python, "
                "[Streamlit](https://streamlit.io) and QRCode.")
    st.markdown("[Github link](https://github.com/dataprojectswithMJ) for those who would like to contribute and "
                "improve this project even further")
    st.markdown("[Email me](mailto:kubeka7712@gmail.com), DM me on [LinkedIn](https://linkedin.com/in/mpho-jan-kubeka) "
                "or [Twitter](https://twitter.com/MphoJKubeka) if you want to work with me. I'm open to new things")

    st.title("")


    with st.expander('Generated code'):
        st.header('Generate code')

        data = st.text_area('What do you want to encode?')
        filename = f'code_{random.randint(1000, 999999)}.png'
        encrypt = st.button('Generate QR code')

        if encrypt:
            img = qrcode.make(data)
            img.save(filename)
            st.image(filename)

            with open(filename, "rb") as file:
                btn = st.download_button(
                    label="Download QR code",
                    data=file,
                    file_name=filename,
                    mime="image/png"
                )

    with st.expander('Decode QR code'):
        upload = st.file_uploader('Upload QR code', type=['png', 'jpg', 'svg'])
        submit = st.button('Decode')
        if upload is not None:
            if submit:
                code = QR(filename=upload.name)
                code.decode()
                st.caption('Hidden message:')
                st.code(code.data)
        else:
            st.error('Upload error')

    return

if __name__ == '__main__':
    main()
