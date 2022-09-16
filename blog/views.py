from django.shortcuts import render

posts=[
    {
        'author':'GabrielDN',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August 27 2018'
    },
    {
        'author':'ReginaMW',
        'title':'Blog Post 2',
        'content':'second Post Content',
        'date_posted':'August 28 2018'
    }
]

def Home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def About(request):
    return render(request,'blog/about.html',{'title':'About'})

