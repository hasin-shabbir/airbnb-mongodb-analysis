import pymongo
connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="mhs581",
                                password="4uUomw6f",
                                authSource="mhs581")
#reference to the collection
collection = connection["mhs581"]["listings"]
#the list of criteria
five_criteria={ "neighbourhood_group_cleansed": "Centro", "beds":{"$gt":2}}
#the projected fields with the id field switched off
five_projection={"_id":0,"name":1,"beds":1,"review_scores_rating":1,"price":1}
#the output using the criteria and projection as arguments to find() and sorting by descending order of review_scores_rating in the five_output variable
five_output=collection.find(five_criteria,five_projection).sort("review_scores_rating",-1)
#output the results to the terminal
for e in five_output:
    print(e)
