FROM jupyter/minimal-notebook

RUN python --version

RUN pip install -U matplotlib \
                   fiona \
                   numexpr \
                   plotly \
                   cufflinks \
                   tables \
                   voila
                   
VOLUME /runbooks
WORKDIR /runbooks
