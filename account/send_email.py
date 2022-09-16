from django.core.mail import send_mail
from movies.models import Movies

def send_confirmation_email(user, code):
    code = code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user
    send_mail(
        'Hello, please activate your account!', 
        f'To activate your account, follow the link: {full_link}',
        'cinem4tic01@gmail.com',
        [to_email,],
        fail_silently=False
    )



def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject', f'Your code for reset password: {code}', 
        'admin@admin.com',[to_email,], fail_silently=False 
    )


def send_notification(user, id):
    to_email = user.email
    send_mail(
        'Order notification!!', 
        f'You have created an order №{id}, please wait for a response!',
        'cinem4tic01@gmail.com',
        [to_email,],
        fail_silently=False
    )


def send_html_email():
    from django.template.loader import render_to_string
    movie = Movies.objects.all()[0]
    html_message = render_to_string('f.html', {'name': movie.name, 
                                    'description': movie.description, 'price': movie.price})
    send_mail(
        'Subject', 
        'Order response', 
        'You have successfully placed an order!', 
        ['cinem4tic01@gmail.com'], 
        html_message=html_message,
        fail_silently=False
    )