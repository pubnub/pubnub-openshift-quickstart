PubNub on OpenShift in 5 Minutes
--------------------------------

This git repository demonstrates how to send messages via PubNub's real-time network on OpenShift using Python.

###Step 1: Create an OpenShift App###

Create an account at http://openshift.redhat.com and set up your local machine with the client tools.

Create a Python-2.7 application (you can call your application whatever you want) and change into the application directory.

<pre>
    rhc app create myapp python-2.7 --from-code https://github.com/openshift/pubnub-openshift-quickstart
    cd myapp
</pre>

###Step 2: Get a PubNub Account###

1. Register at http://www.pubnub.com/free-trial
2. Retrieve your account's publish and subscribe keys
3. Edit the **application** file under **wsgi** folder
4. Replace the **demo** keys in init_pubnub() function
<pre>
    "demo",  # PUBLISH_KEY
    "demo",  # SUBSCRIBE_KEY
</pre>

###Step 3: Deploy your app###
<pre>
    git add .
    git commit -m "my first commmit"
    git push
</pre>

###Step 4: View your app!###
<pre>
    http://myapp-$yournamespace.rhcloud.com
</pre>

More Information
----------------
For PubNub's developer resources visit http://www.pubnub.com/devcenter

For more info on PubNub's Python SDK visit https://github.com/pubnub/python

For all available PubNub SDKs visit: https://github.com/pubnub/pubnub-api
