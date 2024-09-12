from django.views.generic import TemplateView
from django.shortcuts import reverse
import os


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pages = {
            'Главная страница': reverse('home'),
            'Показать текущее время': reverse('time'),
            'Показать содержимое рабочей директории': reverse('workdir')
        }
        context['pages'] = pages
        return context


class WorkdirView(TemplateView):
    template_name = 'app/show_files.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dirs, files = [], []
        for obj in os.listdir('.'):
            if os.path.isdir(os.path.join(os.getcwd(), obj)):
                dirs.append(obj)
            else:
                files.append(obj)
        context = {**context, 'dirs': dirs, 'files': files}
        return context


class WorkdirDetail(TemplateView):
    template_name = 'app/show_detail_files.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_file = self.kwargs['name_file']

        dirs, files = [], []
        for obj in os.listdir(name_file):
            res = os.path.join(os.path.join(os.getcwd(), name_file), obj)
            if os.path.isdir(res):
                dirs.append(res)
            else:
                files.append(res)

        context = {**context,
                   'dirs': zip(dirs, [i.split("\\")[-1] for i in dirs]),
                   'files': [i.split("\\")[-1] for i in files],
                   'name': name_file.split("\\")[-1]}
        return context
