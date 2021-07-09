FROM jupyter/minimal-notebook

RUN python --version

RUN pip install -U fiona \
                   numexpr \
                   plotly \
                   cufflinks \
                   tables 
                   
VOLUME /runbooks
WORKDIR /runbooks
