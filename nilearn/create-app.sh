docker run --rm --entrypoint="" \
    -v $PWD/python:/python
    -v $PWD/temp:/temp
    $APP_NAME sh -c \
    cp -r /usr/lib/python3.6 /python &&
    cp [-r] /path/to/lib /temp                  #copy lib to /temp volume, which is mapped to a filesystem directory $PWD/temp.

# create fspf.pb
docker run -e SCONE_MODE=sim \
    -v $PWD/app:/app \
    -v $PWD/signer:/signer \
    -v $PWD/python/python3.6:/usr/lib/python3.6 \
    -v $PWD/conf:/conf \
    -v $PWD/temp:/temp                                   #maps the directory with lib to authenticate
    iexechub/scone-cli sh -c \

#scone fspf create conf/fspf.pb; \
#scone fspf addr conf/fspf.pb /  --not-protected --kernel /; \
#scone fspf addr conf/fspf.pb /usr/lib/python3.6 --authenticated --kernel /usr/lib/python3.6; \
#scone fspf addf conf/fspf.pb /usr/lib/python3.6 /usr/lib/python3.6;\
#scone fspf addr conf/fspf.pb /usr/bin --authenticated --kernel /usr/bin; \
#scone fspf addf conf/fspf.pb /usr/bin /usr/bin;\
#scone fspf addr conf/fspf.pb /temp/path/to/lib --authenticated --kernel /path/to/lib; \ #authenticate #additional libraries
#scone fspf addf conf/fspf.pb /temp/path/to/lib /path/to/lib;\                           #authenticate #additional libraries
#scone fspf addr conf/fspf.pb /signer --authenticated --kernel /signer; \
#scone fspf addf conf/fspf.pb /signer /signer;\
#scone fspf addr conf/fspf.pb /app --authenticated --kernel /app; \
#scone fspf addf conf/fspf.pb /app /app;\
#scone fspf encrypt ./conf/fspf.pb > /conf/keytag;"

