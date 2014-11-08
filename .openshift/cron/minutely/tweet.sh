if [ $[$RANDOM % 1440] -lt 5 ] ; then
    echo 'tweeting'
    source ${OPENSHIFT_PYTHON_DIR}virtenv/venv/bin/activate
    python ${OPENSHIFT_REPO_DIR}tweet.py
else
    echo 'not tweeting this time'
fi

