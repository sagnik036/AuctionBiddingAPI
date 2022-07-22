# AuctionBiddingAPI
An auction bidding created using django-rest-framework and doccumented using drf-swagger

tools - django-rest-framework and drf_yasg for doccumentations

There are cuurently two users 
1. admin ( Admin)  password - 123 
2. user   (normal user) password - user@123

now to use this api for specific task user need to authenticate themself using jwt tokens

steps for authenctication- 
1. /token/ - here just at the string username pass your username and at password pass your password after that 
             you will recieve one refress and one access key.
             
 2. /token/refresh/ - here using the refress key obtained you can again genrate the access token
 
 
 Now for authentications-
   - click on the Authorize button and at the field 
   - pass - > Bearer apikey/accesstoken
   **note B of Bearer must be Capital and after Bearer a space is required 
   
    for example :
        - access token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxMDI5ODQ0MDA1OCwiaWF0IjoxNjU4NTI2NDU4LCJqdGkiOiJlNjljNmE1ZjAzMWE0MDZmOTRkOTg4ZTQzZTViYzk5OCIsInVzZXJfaWQiOjJ9.HqUnF7t4KHg2t7be_U65tOrbVu3U9PbcDPO6ixnMf-g
        therefore 
         - Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxMDI5ODQ0MDA1OCwiaWF0IjoxNjU4NTI2NDU4LCJqdGkiOiJlNjljNmE1ZjAzMWE0MDZmOTRkOTg4ZTQzZTViYzk5OCIsInVzZXJfaWQiOjJ9.HqUnF7t4KHg2t7be_U65tOrbVu3U9PbcDPO6ixnMf-g

TO USE THE FEATURES GO TO THE FOLLOWING ENDPOINTS-  


Now at  end point - /api/swagger

you will find the swagger doccumentation of the api 

this api has generally this endpoints - 

1. - /auction/bidding/{id}  - here any user without authentication can see the ongoing status of the auction using auction_id
2. - /auction/bidding/{id}  - here user with authentication (using api key i.e jwt token) can bid using auction_id 
3. - /auction/list          - here any user without authentication can see the list of auctions
4. - /auction/list          - here only user with admin rights (i.e authorization) can post the auctions
5. - /auction/status/{id}   - here only user with admin rights can see the status of the auction using auction_id 
6. - /auction/status/{id}   - here only user with admin rights can update the status/infomations of the auctions listed
7. - /auction/status/{id}   - here only user with admin right can delete the auctions lsited

