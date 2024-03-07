from django.shortcuts import render

# Create your views here.
import csv
from app.models import *
from django.http import HttpResponse

def insert_bussiness(self):
    with open('C:\\Users\\ganes\\OneDrive\\Desktop\\Django Projects\\Ganesh\\Scripts\\project29\\app\\Business-employment-data-september-2022-quarter-csv.csv') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            se=i[0]
            p=i[1]
            dv=i[2]
            su=i[3]
            st=i[4]
            un=i[5]
            ma=i[6]
            sub=i[7]
            gr=i[8]
            se_1=i[9]
            se_2=i[10]
            se_3=i[11]
            se_4=i[12]
            se_5=i[13]
            BO=Business(series_refference=se,period=p,data_value=dv,suppressed=su,status=st,units=un,magnitude=ma,subject=sub,group=gr,series_titel_1=se_1,series_titel_2=se_2,series_titel_3=se_3,series_titel_4=se_4,series_titel_5=se_5)
            BO.save()

    return HttpResponse('Bussiness details is insertes sucessfully')