from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from ..models.modelReadingStatus import ReadingStatus
from ..forms import ReadingStatusForm
from ..repository import ReadingStatusRepository

class ReadingStatusListView(View):
    def get(self, request):
        reading_statuses = ReadingStatusRepository.get_all_reading_statuses()
        return render(request, 'reading_status/reading_status_list.html', {'reading_statuses': reading_statuses})

class ReadingStatusDetailView(View):
    def get(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        return render(request, 'reading_status/reading_status_detail.html', {'reading_status': reading_status})

class ReadingStatusCreateView(View):
    def get(self, request):
        form = ReadingStatusForm()
        return render(request, 'reading_status/reading_status_form.html', {'form': form})

    def post(self, request):
        form = ReadingStatusForm(request.POST)
        if form.is_valid():
            reading_status = ReadingStatusRepository.create_reading_status(form.cleaned_data)
            return redirect('reading-status-detail', pk=reading_status.id)
        return render(request, 'reading_status/reading_status_form.html', {'form': form})

class ReadingStatusUpdateView(View):
    def get(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        form = ReadingStatusForm(instance=reading_status)
        return render(request, 'reading_status/reading_status_form.html', {'form': form, 'reading_status': reading_status})

    def post(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        form = ReadingStatusForm(request.POST, instance=reading_status)
        if form.is_valid():
            ReadingStatusRepository.update_reading_status(reading_status, form.cleaned_data)
            return redirect('reading-status-detail', pk=reading_status.id)
        return render(request, 'reading_status/reading_status_form.html', {'form': form, 'reading_status': reading_status})

class ReadingStatusDeleteView(View):
    def get(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        return render(request, 'reading_status/reading_status_confirm_delete.html', {'reading_status': reading_status})

    def post(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        ReadingStatusRepository.delete_reading_status(reading_status)
        return redirect('reading-status-list')