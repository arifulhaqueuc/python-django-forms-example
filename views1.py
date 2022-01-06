from django.views.generic.edit import FormMixin
class SomePageView(FormMixin, ListView):
    template_name = "homepage.html"
    form_class = GuestResumeForm
    msg_succ = 'your resume submitted successfully'
    model = SomeModelName
    success_url = reverse_lazy('fileupload_success_url')


    def get_queryset(self):
        return model.objects.all()


    def post(self, request, *args, **kwargs):
        # form_class = self.get_form_class()
        # form = self.get_form(form_class)
        form = GuestResumeForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        super().form_valid(form)
        given_email = form.cleaned_data['email']
        print(given_email)
        form.save()
        messages.success(self.request, self.msg_succ)
        messages.success(self.request, given_email)
        subject=''
        msg=''
        sender=''
        recipients=''
        # send_mail(subject=subject, message=msg, sender=sender, recipients=recipients)
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        form = SomeForm()
        return HttpResponse('im from line#41 views.py')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {}

        return context

