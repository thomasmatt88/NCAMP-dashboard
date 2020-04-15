# NCAMP-dashboard
NCAMP, the National Center for Advanced Materials Performance, works with the FAA and industry partners to qualify material systems and populate a shared materials database that can be viewed publicly. This is a dashboard for viewing NCAMP materials database. 

[NCAMP-dashboard](https://ncamp-dashboard.herokuapp.com)

**1. Select a material**<br/>
Select an NCAMP qualified material from the top dropdown. Tables will update below with metadata, physical properties, and mechanical properties of chosen material. If only one material is chosen, then a similar material will be recommended. Similarity is determined based off of minimum Euclidean Distance from selected material. 
<br/>
<br/>
![select](https://user-images.githubusercontent.com/49013120/79288446-9e4ac980-7e7b-11ea-83af-52dd5fc91efe.gif)
<br/>
<br/>
**2. Select all materials**<br/>
<br/>
<br/>
![selectallmat](https://user-images.githubusercontent.com/49013120/79289371-e9fe7280-7e7d-11ea-820b-9612b68f4964.gif)
<br/>
<br/>
**3. Show predicted material properties**<br/>
We can infer unmeasured material properties using machine learning. Use toggle switch to show or not show these predicted material properties. 
<br/>
<br/>
![pred](https://user-images.githubusercontent.com/49013120/79289616-9e989400-7e7e-11ea-8a3e-45b6dd10dd26.gif)
<br/>
<br/>
**4. Filter materials**<br/>
Narrow down qualified materials and qualified material properties using filters.  
<br/>
<br/>
![filter](https://user-images.githubusercontent.com/49013120/79290146-27fc9600-7e80-11ea-9d49-36b958ae64bd.gif)
