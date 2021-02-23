FROM python:3
LABEL maintainer='Henri Vandersleyen' 
LABEL maintainerEmail='hvandersleyen@gmail.com'
WORKDIR /usr/src/app
# copy to make usage of caching
COPY requirements.txt ./

#install dependencies
RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uswsgi",'app.ini']