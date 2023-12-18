from django.shortcuts import render,HttpResponse
from .models import *



def home(request):
    emp = employee_master.objects.all()
    for x in emp:
        try:
            user = User.objects.get(employee_master=x)
            user.employee_master = x
            user.username = str(x.employee_id)
            user.save()
        except User.DoesNotExist:
            new_user = User.objects.create(username=str(x.employee_id), password='1234',employee_master=x)
    return HttpResponse('Data Created')


#---------------------Aggregation and Annotate-------------------------
# USE CODE IN SHELL


# Total number of books.
# >>> Book.objects.count()
# 2452

# # Total number of books with publisher=BaloneyPress
# >>> Book.objects.filter(publisher__name="BaloneyPress").count()
# 73

# # Average price across all books.
# >>> from django.db.models import Avg
# >>> Book.objects.aggregate(Avg("price"))
# {'price__avg': 34.35}

# # Max price across all books.
# >>> from django.db.models import Max
# >>> Book.objects.aggregate(Max("price"))
# {'price__max': Decimal('81.20')}

# # Difference between the highest priced book and the average price of all books.
# >>> from django.db.models import FloatField
# >>> Book.objects.aggregate(
# ...     price_diff=Max("price", output_field=FloatField()) - Avg("price")
# ... )
# {'price_diff': 46.85}

# # All the following queries involve traversing the Book<->Publisher
# # foreign key relationship backwards.

# # Each publisher, each with a count of books as a "num_books" attribute.
# >>> from django.db.models import Count
# >>> pubs = Publisher.objects.annotate(num_books=Count("book"))
# >>> pubs
# <QuerySet [<Publisher: BaloneyPress>, <Publisher: SalamiPress>, ...]>
# >>> pubs[0].num_books
# 73

# # Each publisher, with a separate count of books with a rating above and below 5
# >>> from django.db.models import Q
# >>> above_5 = Count("book", filter=Q(book__rating__gt=5))
# >>> below_5 = Count("book", filter=Q(book__rating__lte=5))
# >>> pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
# >>> pubs[0].above_5
# 23
# >>> pubs[0].below_5
# 12

# # The top 5 publishers, in order by number of books.
# >>> pubs = Publisher.objects.annotate(num_books=Count("book")).order_by("-num_books")[:5]
# >>> pubs[0].num_books
# 1323


















