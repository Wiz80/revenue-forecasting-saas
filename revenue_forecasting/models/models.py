from django.db import models

# Create your models here.
# class NetflixRevenue(models.Model):
#     date = models.DateField()
#     global_revenue = models.BigIntegerField()
#     ucan_streaming_revenue = models.BigIntegerField()
#     emea_streaming_revenue = models.BigIntegerField()
#     latm_streaming_revenue = models.BigIntegerField()
#     apac_streaming_revenue = models.BigIntegerField()
#     ucan_members = models.IntegerField()
#     emea_members = models.IntegerField()
#     latm_members = models.IntegerField()
#     apac_members = models.IntegerField()
#     ucan_arpu = models.DecimalField(max_digits=5, decimal_places=2)
#     emea_arpu = models.DecimalField(max_digits=5, decimal_places=2)
#     latm_arpu = models.DecimalField(max_digits=5, decimal_places=2)
#     apac_arpu = models.DecimalField(max_digits=5, decimal_places=2)
#     netflix_streaming_memberships = models.BigIntegerField()

#     def __str__(self):
#         return f"{self.date} Revenue"