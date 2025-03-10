from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils.html import format_html

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    form=UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('email')
            user_name = form.cleaned_data.get('name')
            company = form.cleaned_data.get('company', 'N/A')  # Optional field
            message = form.cleaned_data.get('message')

            # # Construct email content
            # subject = f"New Contact Form Submission from {user_name}"
            # email_body = f"""
            # Name: {user_name}
            # Company: {company}
            # Email: {user_email}
            # Message: {message}
            # """

            # # Send email (From user's email)
            # send_mail(
            #     subject,
            #     email_body,
            #     user_email,  # User's email as the sender
            #     ['ganjanee2003@gmail.com'],  # Replace with your receiving email
            #     # reply_to=[user_email],
            #     fail_silently=False,
            # )
            email_body = format_html(
                """
                <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ddd; border-radius: 8px; max-width: 500px;">
                    <h2 style="color: #0073e6;">🌟 New Contact Submission 🌟</h2>
                    <p><strong>Name:</strong> {}</p>
                    <p><strong>Company:</strong> {}</p>
                    <p><strong>Email:</strong> <a href="mailto:{}" style="color: #0073e6;">{}</a></p>
                    <p><strong>Message:</strong> <em>"{}"</em></p>
                    <hr>
                    <p style="color: #666;">📩 Reply directly to this email to contact {}</p>
                </div>
                """,
                user_name, company, user_email, user_email, message, user_name
            )

            # Create & send email
            email = EmailMessage(
                subject=f"New Contact Form Submission from {user_name}",
                body=email_body,
                from_email='gundalaanjaneedevi@gmail.com',
                to=['ganjanee2003@gmail.com'],  
                reply_to=[user_email],
            )
            email.content_subtype = "html"  # Set content type to HTML
            email.send(fail_silently=False)
    return render(request,'contact.html',{'data':form})