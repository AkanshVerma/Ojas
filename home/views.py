from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def physical(request):
    return render(request, 'latestphysical.html')

def mental(request):
    return render(request, 'mental.html')

def bmi(request):
    student_bmi = ''
    try:
        if request.method == 'POST':
            student_height = eval(request.POST['height'])
            student_weight = eval(request.POST['weight'])
            student_bmi = student_weight / student_height ** 2

    except:
        pass

    return render(request, 'bmi.html', {'output':student_bmi})

def wellbeing(request):
    return render(request, 'wellbeing.html')

def login(request):
    return render(request, 'login.html')

def underWeight(request):

    data = {
        'n_monday':['3 onion stuffed parantha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','1 cup moong dal/ chicken curry + 1 cup potato and caulifllower vegetable + 3 chapatti + 1/2 cup rice + salad','cup beans potato vegetable + 3 chapatti + salad'],

        'n_tuesday':['3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad','cup carrot peas vegetable +3 chapatti + salad'],

        'n_wednesday':['1.5 cup vegetable bread upma + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','Lunch-1 cup rajma curry + 1 cup spinach potato + 3 chapatti + 1/2 cup rice + salad','1.5 cup parwal vegetable + 3 chapatti + salad'],

        'n_thursday':['2 cucumber potato sandwich + 1 tsp green chutney + 1 orange juice + 3 cshews + 2 walnuts + 4 almonds','cup white chana/ fish curry + 3 chapatti + 1/2 cup rice + salad','1 cup cauliflower potato vegetable + 3 chapatti + salad'],

        'n_friday':['2 cup vegetable poha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','cup chana dal + 1 cup bhindi vegetable + 3 chapatti + 1/2 cup rice + salad','cup peas mushroom vegetable + 3 chapatti +salad'],

        'n_saturday':['3 vegetable suji cheela + 1 cup strawberry shake + 4 cashews + 4 almonds + 3 walnuts','1 cup mix dal + 1 cup soybean curry + 3 chapatti + 1/2 cup curd + salad','1 cup karela vegetable + 3 chaptti + salad'],

        'n_sunday':['2 egg brown bread sandwich + green chutney + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','1 cup arhar dal + 1 cup potato curry + 3 chapatti + 1/2 cup rice + 1/2 cup low fat curd + salad','1.5 cup chicken curry + 3 chapatti + salad'],

        'monday':['3 onion stuffed parantha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','1 cup moong dal + 1 cup potato and caulifllower vegetable + 3 chapatti + 1/2 cup rice + salad','1 cup beans potato vegetable + 3 chapatti + salad'],
        'tuesday':['3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad','1 cup carrot peas vegetable +3 chapatti + salad'],
        'wednesday':['1.5 cup vegetable bread upma + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','1 cup rajma curry + 1 cup spinach potato + 3 chapatti + 1/2 cup rice + salad','1.5 cup parwal vegetable + 3 chapatti + salad'],
        'thursday':['2 cucumber potato sandwich + 1 tsp green chutney + 1 orange juice + 3 cshews + 2 walnuts + 4 almonds','1 cup white chana + 3 chapatti + 1/2 cup rice + salad','1 cup cauliflower potato vegetable + 3 chapatti + salad'],
        'friday':['2 cup vegetable poha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','1 cup chana dal + 1 cup bhindi vegetable + 3 chapatti + 1/2 cup rice + salad','1 cup peas mushroom vegetable + 3 chapatti + salad'],
        'saturday':['3 vegetable suji cheela + 1 cup strawberry shake + 4 cashews + 4 almonds + 3 walnuts','1 cup mix dal + 1 cup soybean curry + 3 chapatti + 1/2 cup curd + salad','1 cup karela vegetable + 3 chaptti + salad'],
        'sunday':['2 brown bread sandwich + green chutney + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','1 cup arhar dal + 1 cup potato curry + 3 chapatti + 1/2 cup rice + 1/2 cup low fat curd + salad','Panner Dish + 3 chapatti + salad']
    }

    return render (request, 'underweight.html', data)

def normal(request):
    data1 ={
        'n_monday':['1 onion stuffed chapatti + 1/2 cup low fat curd','1 cup moong dal/ chicken curry + 1 chapatti + salad','1 cup beans + 1 chapatti + salad'],

        'n_tuesday':['3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad','cup carrot peas vegetable +3 chapatti + salad'],

        'n_wednesday':['1 cup vegetable brown bread upma + 1/2 cup low fat milk (no sugar)','1 cup rajma curry + 1 chapatti + salad','1 cup parwal vegetable + 1 chapatti + salad'],

        'n_thursday':['1 cucumber hungcurd sandwich + 1/2 tsp green chutney + 1 orange','1 cup white chana/ fish curry + 1 chapatti + salad','1 cup cauliflower vegetable + 1 chapatti + salad'],

        'n_friday':['1 cup vegetable poha + 1 cup low fat curd','1 cup chana dal + 1 chapatti + salad','1 cup tinda vegetable + 1 chapatti + salad'],

        'n_saturday':['3 vegetable suji cheela + 1 cup strawberry shake + 4 cashews + 4 almonds + 3 walnuts','1 cup mix dal + 1 cup soybean curry + 3 chapatti + 1/2 cup curd + salad','1 cup karela vegetable + 3 chaptti + salad'],

        'n_sunday':['2 egg brown bread sandwich + green chutney + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','cup arhar dal + 1 cup potato curry + 3 chapatti + 1/2 cup rice + 1/2 cup low fat curd + salad','1.5 cup chicken curry + 3 chapatti + salad'],

        'monday':['1 onion stuffed chapatti + 1/2 cup low fat curd','1 cup moong dal + 1 chapatti + salad','1 cup beans + 1 chapatti + salad'],
        'tuesday':['3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts','1 cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad','1 cup carrot peas vegetable +3 chapatti + salad'],
        'wednesday':['1 cup vegetable brown bread upma + 1/2 cup low fat milk (no sugar)','1 cup rajma curry + 1 chapatti + salad','1 cup parwal vegetable + 1 chapatti + salad'],
        'thursday':['1 cucumber hungcurd sandwich + 1/2 tsp green chutney + 1 orange','1 cup white chana + 1 chapatti + salad','1 cup cauliflower vegetable + 1 chapatti + salad'],
        'friday':['1 cup vegetable poha + 1 cup low fat curd','1 cup chana dal + 1 chapatti + salad','1 cup tinda vegetable + 1 chapatti + salad'],
        'saturday':['3 vegetable suji cheela + 1 cup strawberry shake + 4 cashews + 4 almonds + 3 walnuts','1 cup mix dal + 1 cup soybean curry + 3 chapatti + 1/2 cup curd + salad','1 cup karela vegetable + 3 chaptti + salad'],
        'sunday':['2 brown bread sandwich + green chutney + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts','1 cup arhar dal + 1 cup potato curry + 3 chapatti + 1/2 cup rice + 1/2 cup low fat curd + salad','1 Panner Dish + 3 chapatti + salad']
    }
    
    return render(request, 'normal.html', data1)

def overweight(request):

    data2= {
        'n_monday':['1 onion stuffed chapatti + 1/2 cup low fat curd','1 cup moong dal/ chicken curry + 1 chapatti + salad','1 cup beans + 1 chapatti + salad'],

        'n_tuesday':['2 besan cheela + 1/2 cup low fat curd','1 cup masoor dal + 1 chapatti + 1/2 up low fat curd + salad','1 cup carrot peas vegetable +1 chapatti + salad'],

        'n_wednesday':['1 cup vegetable brown bread upma + 1/2 cup low fat milk (no sugar)','1 cup rajma curry + 1 chapatti + salad','1 cup parwal vegetable + 1 chapatti + salad'],

        'n_thursday':['1 cucumber hungcurd sandwich + 1/2 tsp green chutney + 1 orange','1 cup white chana/ fish curry + 1 chapatti + salad','1 cup cauliflower vegetable + 1 chapatti + salad'],

        'n_friday':['1 cup vegetable poha + 1 cup low fat curd','1 cup chana dal + 1 chapatti + salad','1 cup tinda vegetable + 1 chapatti + salad'],

        'n_saturday':['1 cup low fat milk with oats + 3-4 strawberries','1 cup soybean curry + 1 chapatti + 1/2 cup low fat curd + salad','1 cup ghia vegetable + 1 chaptti + salad'],

        'n_sunday':['3 egg whites + 1 toasted brown bread + 1/2 cup low fat milk (no sugar)','1 cup arhar dal + 1 chapatti + 1/2 cup low fat curd + salad','1 cup pumpkin + 1 chapatti + salad'],

        'monday':['1 onion stuffed chapatti + 1/2 cup low fat curd','1 cup moong dal+ 1 chapatti + salad','1 cup beans + 1 chapatti + salad'],
        'tuesday':['2 besan cheela + 1/2 cup low fat curd','1 cup masoor dal + 1 chapatti + 1/2 up low fat curd + salad','1 cup carrot peas vegetable +1 chapatti + salad'],
        'wednesday':['1 cup vegetable brown bread upma + 1/2 cup low fat milk (no sugar)','1 cup rajma curry + 1 chapatti + salad','1 cup parwal vegetable + 1 chapatti + salad'],
        'thursday':['1 cucumber hungcurd sandwich + 1/2 tsp green chutney + 1 orange','1 cup white chana + 1 chapatti + salad','1 cup cauliflower vegetable + 1 chapatti + salad'],
        'friday':['1 cup vegetable poha + 1 cup low fat curd','1 cup chana dal + 1 chapatti + salad','1 cup tinda vegetable + 1 chapatti + salad'],
        'saturday':['1 cup low fat milk with oats + 3-4 strawberries','1 cup soybean curry + 1 chapatti + 1/2 cup low fat curd + salad','1 cup ghia vegetable + 1 chaptti + salad'],
        'sunday':['1 toasted brown bread + 1/2 cup low fat milk (no sugar)','1 cup arhar dal + 1 chapatti + 1/2 cup low fat curd + salad','1 cup pumpkin + 1 chapatti + salad']
    }
    return render(request, 'overweight.html', data2)

