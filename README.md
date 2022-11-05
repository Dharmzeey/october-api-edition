# october-api-edition
This is the submission for dennisivy api edition octoer hackathon competition.

##
It is an api that contains Advocates with the countries they work with

Api calls can be made to two major endpoints, Advocate and Companies

## Advocate
### This contains advocates list
+ The API calls calls can be made to list out all the advocates using the `` domain/advocates/ `` 

+ The API is paginated with 100 response per page, calls can be with pagination with 
`` domain/advocates/?limit=100&offset=next100 `` example `` https://dharmzeey-october-api.up.railway.app/advocates/?limit=100&offset=100 `` or `` https://dharmzeey-october-api.up.railway.app/advocates/?limit=100&offset=400 ``

+ API call can be made to search for the username using the `` domain/advocates/:username `` example `` https://dharmzeey-october-api.up.railway.app/advocates/dharmzeey/ `` will fetch the detail for the username provided that it exist

+ Also API calls can also be used to query the advocates list if it contains the query being searched using the `` domain/advocates/?query=search_keyword `` example `` https://dharmzeey-october-api.up.railway.app/advocates/?query=adam `` this will return items which contains the searched keywords (adam) in its username of name else returns the whole advocates like normal


## Comany
### This contains Company list
+ The API calls calls can be made to list out all the company using the `` domain/companies/ `` 

+ The API is paginated with 100 response per page, calls can be with pagination with 
`` domain/companies/?limit=100&offset=next100 `` example `` https://dharmzeey-october-api.up.railway.app/companies/?limit=100&offset=100 `` or `` https://dharmzeey-october-api.up.railway.app/companies/?limit=100&offset=400 ``

+ Also API calls can be used to query the companies list if it contains the query being searched using the `` domain/companies/?query=search_keyword `` example `` https://dharmzeey-october-api.up.railway.app/companies/?query=Dharmzeey `` this will return items which contains the searched keywords (Dharmzeey) in its name else returns the whole companies like normal

# Enjoy 😎😋
[Visit API](https://dharmzeey-october-api.up.railway.app/)