from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

from .models import Applications, Sherbime, Formular, BazaLigjore, TestZone, Manuale, Post, About, ApplicationsPost, \
    MostUsedApp


# Create your views here.


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = 'albiona.durmishi@asp.gov.al'#request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            settings.DEFAULT_FROM_EMAIL,  # from email
            [message_email],  # to email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def applications(request):
    # applications = Entry.objects.filter(type="application")

    applications = Applications.objects.all().order_by('order')
    formulars = Formular.objects.all
    tests = TestZone.objects.all
    manuales = Manuale.objects.all
    sherbimes = Sherbime.objects.all
    bazaligjores = BazaLigjore.objects.all
    applicationsposts = ApplicationsPost.objects.all

    context = {'applications': applications, 'formulars': formulars, 'tests': tests, 'manuales': manuales,
               'sherbimes': sherbimes, 'bazaligjores': bazaligjores, 'applicationsposts': applicationsposts}
    return render(request, "applications.html", context)


def home(request):
    post = Post.objects.all().order_by('-pk')[:6]
    mostusedapp = MostUsedApp.objects.all

    context = {'post': post, 'mostusedapp': mostusedapp}
    return render(request, 'home.html', context)


def about(request):
    about = About.objects.all
    return render(request, 'about.html', {'about': about})


def sherbime(request):
    return render(request, 'home.html')


def applicationspost(request):
    return render(request, 'home.html')


def manuale(request):
    return render(request, 'home.html')


def formular(request):
    return render(request, 'home.html')


def bazaligjore(request):
    return render(request, 'home.html')


def testzone(request):
    return render(request, 'home.html')


def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        applications = Applications.objects.all().filter(title__icontains=search)
        formulars = Formular.objects.all().filter(title__icontains=search)
        tests = TestZone.objects.all().filter(title__icontains=search)
        manuales = Manuale.objects.all().filter(title__icontains=search)
        sherbimes = Sherbime.objects.all().filter(title__icontains=search)
        bazaligjores = BazaLigjore.objects.all().filter(title__icontains=search)
        applicationsposts = ApplicationsPost.objects.all().filter(title__icontains=search)
        post = Post.objects.all().filter(title__icontains=search)

        context = {'applications': applications, 'formulars': formulars, 'tests': tests, 'manuales': manuales,
                   'sherbimes': sherbimes, 'bazaligjores': bazaligjores, 'applicationsposts': applicationsposts,
                   'post': post}
        return render(request, "searchbar.html", context)
