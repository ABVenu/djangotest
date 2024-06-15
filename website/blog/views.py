from django.shortcuts import render

# Create your views here.

def blogsList(request):
    blogs = [
    {"id":1,"name":"Learn JS","author":"James","desc":"This is about learning JS"},
    {"id":2,"name":"Learn Django","author":"John","desc":"This is about learning Django"},
    {"id":3,"name":"Learn React","author":"Jimmy","desc":"This is about learning React"}
]
    return render(request,"blog/blogList.html",{"blogsList":blogs})

def blogDetails(request,id):
    blogs = {
        1:{"name":"Learn JS","author":"James","desc":"This is about learning JS"},
        2:{"name":"Learn Django","author":"John","desc":"This is about learning Django"},
        3:{"name":"Learn React","author":"Jimmy","desc":"This is about learning React"}
    }
    detailedBlog = blogs.get(id)
    # print(detailedBlog)
    return render(request,"blog/blogDetails.html",{"blog":detailedBlog})