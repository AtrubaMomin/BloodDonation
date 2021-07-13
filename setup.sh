mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"atroobamomin7@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 8001\n\
" > ~/.streamlit/config.toml
