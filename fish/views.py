from django.shortcuts import render, redirect
from fish.forms import DuoForm

def main_list(request):
    return render(request, 'relevant_info.html')

def success(request):
    return render(request, 'success.html')

# регистрация сквадов на бесплатный турнир
def squads_reg(request):
    if request.method == "POST":
        form = DuoForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.save()
            return redirect('success')
    else:
        form = DuoForm()
    return render(request, 'authVK.html', {'form': form})
