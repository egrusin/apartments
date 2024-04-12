from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import MultistoreyBuilding
from .forms import MultistoreyBuildingForm


@csrf_exempt
def add_building(request):
    if request.method == 'POST':
        form = MultistoreyBuildingForm(request.POST)
        if form.is_valid():
            if form.check_area():
                # Получаем данные из POST-запроса
                data = request.POST
                fias_code = data.get('fias_code')
                wall_material = data.get('wall_material')
                year_built = data.get('year_built')
                area = data.get('area')
                apartments_count = data.get('apartments_count')

                # Создаем новый объект и сохраняем его в базе данных
                MultistoreyBuilding.create(
                    fias_code=fias_code,
                    wall_material=wall_material,
                    year_built=int(year_built),
                    area=float(area),
                    apartments_count=int(apartments_count)
                )

                # Возвращаем ответ
                return HttpResponse("<h3>Дом успешно зарегистрирован</h3>")
            form.add_error("area", "Некорректное значение площади")
        else:
            form.add_error(None, "Заполните всю форму")
    else:
        form = MultistoreyBuildingForm()

    context = {'form': form}
    return render(request, 'static/build_form.html', context)


@csrf_exempt
def building_detail(request, id):
    building = MultistoreyBuilding.get(id)
    return render(request, 'static/building_detail.html', {'building': building})
