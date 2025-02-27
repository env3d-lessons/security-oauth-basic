# Setup

This assignment will be completed on our class shared server,
`learn.operatoroverload.com`.  You will need to login
to the server and clone this repo into your `${HOME}/public_html/`
directory.  The process is similar to the following (replace
the variables with your own values):

```bash 
$ ssh ${USERID}@learn.operatoroverload.com
$ cd public_html
$ git clone ${ASSIGNMENT_REPO}
$ cd ${ASSIGNMENT_REPO}
```

If you have done everything correct, you should be able to access
your index.html page using the url:

```
https://learn.operatoroverload.com/${USERID}/${ASSIGNMENT_REPO}/
```

# Introduction

Goal: Create your own “Login via Google” button

First, study the example at https://github.com/env3d/oauth-basic-tutorial.
The index.html file is a very basic (but functional) example of how you can
login to Facebook using the OAuth 2.0 protocol.

This repo contains the same `index.html` as the facebook example.  Your
job is to modify this example to work with google.

It turns out many major cloud providers (such as Google, Apple, etc.)
also act as identity providers.  This assignment will have you modify the
Facebook example so it'll work with Google instead.

To see how the Google login works, use the Google OAuth 2.0 playground
https://developers.google.com/oauthplayground/ app.  It contains the same
steps that's illustrated in my example above.

NOTE: In this assignment, we are implementing the OAuth 2.0 flow manually,
which is NOT RECOMMENDED for production systems as the protocol is very
complex.  In a production environment, use SDKs provided by various vendors
such as Firebase, passport.js, etc.

# Steps

  1. Go to https://console.developers.google.com and register a new project
  
  1. For now, do not enable any additional API and services, as we will simply
     be using google for authentication (OpenID Connect)

  1. Under the "Credentials" menu, select the "OAuth Consent Screen" tab and make
     sure you fill in the scope and “Authorized Domains” section so google can
     redirect back to your site.

     ![Credentials](images/image3.png)

  1. Go back to the "credentials" tab and select
     "Create credentials" -> "OAuth Client ID" to create a
     "Client ID/Client Secret" pair.

  1. Be sure to fill out the "Authorized Javascript Origin" and
     "Authorized Redirect URL"!  The Authorized Redirect URL will
     be the URL of your index.html file.

     ![Credentials](images/image2.png)

  1. Now that your google oauth2 client is set up, you are ready to code.  
     Below are the few things you need to change in the index.html file
     so it'll work with Google:
      - Change the client ID to your app's client id
      - In step 1
        - The google login url is https://accounts.google.com/o/oauth2/v2/auth
        - In the scope field, Instead of the `public_profile`, Google's scope is simply `profile`
      - In step 2
        - Retrieve the token from the URL fragment
      - In step 3
        - Google's userinfo endpoint is at https://openidconnect.googleapis.com/v1/userinfo 
        - The json returned has a slightly different structure

  1. The end result should look something like this:

     ![Result](images/image1.gif)


# Hand-in

Execute pytest in your `${HOME}/public_html/${ASSIGNMENT_REPO}/` to check if you got 
everything correct.

When you are satisified, run the following commands to submit:

  - git add -A
  - git commit -a -m 'submit'
  - git push

