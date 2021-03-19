from django.shortcuts import get_object_or_404, render

from .models import Osoba, Telefon, Email

def emile_i_telefony_osob(lista_osob):
    kontakty_lista = []
    for osoba in lista_osob:
        telefony = Telefon.objects.filter(osoba=osoba)
        emaile = Email.objects.filter(osoba=osoba)
        kontakty_lista.append([osoba, telefony, emaile])
    return kontakty_lista

def poprawnie_przeslany_parametr(param):
    return param != '' and param is not None

def index(request):
    lista_osob = Osoba.objects.all()
    kontakty_wyjscie = emile_i_telefony_osob(lista_osob)
    context = {'contact_list': kontakty_wyjscie}
    return render(request, 'polls/index.html', context)

def deleteContact(request,pk):
    osoba = Osoba.objects.filter(id=pk)
    telefony = Telefon.objects.filter(osoba=osoba[0])
    emaile = Email.objects.filter(osoba=osoba[0])

    if len(telefony)==0 and len(emaile)==0:
       osoba.delete()
    return index(request)

def newContact(request):
    imie = request.POST.get('imie')
    nazwisko = request.POST.get('nazwisko')

    if not poprawnie_przeslany_parametr(imie):
        return index(request)
    elif not poprawnie_przeslany_parametr(nazwisko):
        return index(request)

    newPerson = Osoba.objects.create(imie=imie,nazwisko=nazwisko)

    return index(request)

def addEmail(request,osoba_pk):
    osoba = Osoba.objects.filter(id=osoba_pk)
    Email.objects.create(osoba=osoba[0],email=request.POST.get('newEmail'))
    return index(request)

def addPhone(request,osoba_pk):
    Telefon.objects.create(osoba=Osoba.objects.filter(id=osoba_pk)[0],
                           telefon=request.POST.get('newPhone'))
    return index(request)

def editContact(request,osoba_pk):
    osoba = Osoba.objects.filter(id=osoba_pk)[0]
    imie = request.POST.get("osobaImie")
    nazwisko = request.POST.get("osobaNazwisko")
    if osoba.imie != imie:
        osoba.imie = imie
    if osoba.nazwisko != nazwisko:
        osoba.nazwisko = nazwisko
    osoba.save()
    return index(request)



def findContact(request):
    imiePost =  request.POST.get("findImie")
    print(imiePost)
    nazwiskoPost = request.POST.get("findNazwisko")
    print(nazwiskoPost)
    emailPOST = request.POST.get("findEmail")
    print(emailPOST)
    telefonPOST = request.POST.get("findTelefon")
    print(telefonPOST)
    if not poprawnie_przeslany_parametr(telefonPOST) \
            and not poprawnie_przeslany_parametr(emailPOST)\
            and not poprawnie_przeslany_parametr(nazwiskoPost)\
            and not poprawnie_przeslany_parametr(imiePost):
        return index(request)

    emaile = Email.objects.all()
    telefony = Telefon.objects.all()
    osoby = Osoba.objects.all()


    if poprawnie_przeslany_parametr(imiePost):
        osoby = osoby.filter(imie__icontains=imiePost)
        print("valid imiePost: ")
        print(osoby)

    if poprawnie_przeslany_parametr(nazwiskoPost):
        osoby = osoby.filter(nazwisko__icontains=nazwiskoPost)
        print("valid nazwiskoPost: ")
        print(osoby)

    if poprawnie_przeslany_parametr(emailPOST):
        emaile = emaile.filter(email__icontains=emailPOST)
        email_osoby = []
        for osoba in osoby:
            for email in emaile:
                if osoba == email.osoba:
                    email_osoby.append(osoba)
        osoby = email_osoby

    if poprawnie_przeslany_parametr(telefonPOST):
        telefony = telefony.filter(telefon__icontains=telefonPOST)
        telefon_osoby = []
        for osoba in osoby:
            for telefon in telefony:
                if osoba == telefon.osoba:
                    telefon_osoby.append(osoba)
        osoby = telefon_osoby

    lista_kontaktow = emile_i_telefony_osob(osoby)
    
    context = {'lista_kontaktow': lista_kontaktow}
    return render(request, 'polls/index.html', context)