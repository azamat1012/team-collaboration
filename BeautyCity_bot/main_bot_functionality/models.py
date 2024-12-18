from django.db import models


# class Salon(models.Model):
#         .......


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Продолжительность услуги в минутах")
    category = models.CharField(
        max_length=200,
        choices=[
            ('Стрижка волос', 'Стрижка волос'),
            ('Борода', 'Борода'),
            ('Укладка волос', 'Укладка волос'),
            ('Окрашивание волос', 'Окрашивание волос'),
            ('Уход за лицом', 'Уход за лицом'),
        ]

    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Specialist(models.Model):
    name = models.CharField(max_length=200)
    biography = models.CharField(max_length=200, null=True, blank=True)
    specialization = models.CharField(
        max_length=200,
        choices=[
            ('Стрижка волос', 'Стрижка волос'),
            ('Борода', 'Борода'),
            ('Укладка волос', 'Укладка волос'),
            ('Окрашиванаие волос', 'Окрашиванаие волос'),
            ('Уход за лицом', 'Уход за лицом'),
        ])
    # salon = models.ForeignKey(Salon, on_delete=models.CASCADE, null=True, related_name="specialists")      ------->  ждем модель Salon
    availability = models.BooleanField(default=True)
    # rating - можно добавить в дальнейшем

    def __str__(self):
        return self.name


class Appointment(models.Model):
    client_name = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=12)
    # service = models.ForeignKey(
    #     Service, on_delete=models.CASCADE, null=True, related_name="appointments")                               -------> ждем модель Service
    # salon = models.ForeignKey(Salon, on_delete=models.CASCADE, null=True, related_name="appointments")           -------> ждем модель Salon
    location = models.CharField(max_length=100)
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, null=True, related_name="appointments")
    start_session = models.DateTimeField()
    end_session = models.DateTimeField()

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['-start_session', '-end_session']


class Payment(models.Model):
    # Модель для инфы о платежах

    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, null=True, related_name="payments")
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, null=True, related_name="payments")
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.payment_method


class Notification(models.Model):
    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, null=True, related_name="notifications")
    message = models.TextField(null=True, blank=True)
    send_at = models.DateTimeField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-send_at']


class SalonManager(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    number = models.IntegerField()
