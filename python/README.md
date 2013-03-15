PubNub on OpenShift
===================

This git repository demonstrates how to send messages via PubNub on OpenShift using Python.


Running on OpenShift
--------------------

Create a free PubNub account at http://www.pubnub.com/free-trial to get publish and subscribe keys.

Create an account at http://openshift.redhat.com and set up your local machine with the client tools.

Create a Python-2.7 application (you can call your application whatever you want)
<pre>
    rhc app create myapp python-2.7
</pre>
Add this upstream PubNub repo
<pre>
    cd pubnub
    git remote add upstream -m master https://github.com/pubnub/openshift/python
    git pull -s recursive -X theirs upstream master
</pre>

###Configuration###
Replace the <strong>"demo"</strong> keys specified within the init_pubnub() function (<strong>python/wsgi/application</strong> file) with your own account publish and subscribe keys:

    "demo",  # PUBLISH_KEY
    "demo",  # SUBSCRIBE_KEY

Then push the repo
<pre>
    git add .
    git commit -m "my first commmit"
    git push
</pre>

That's it, you can now see your application at:
<pre>
    http://myapp-$yournamespace.rhcloud.com
</pre>

For more details about PubNub's Python SDK, please read https://github.com/pubnub/python/tree/master/python
You can also create PubNub Quickstarts for other programming languages, such as PHP, Ruby, Node.JS and more. 
