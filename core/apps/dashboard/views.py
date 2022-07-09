from django.shortcuts import render, get_object_or_404,redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.forms import formset_factory
from extensions import jalali
import datetime
import plotly.express as px
import MySQLdb
import pandas as pd


@login_required
def panel(request):
    conn = MySQLdb.connect(host="localhost", user="keybaanc_admin", passwd="@Code4760", db="keybaanc_db")
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish<"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish))*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-03-21" AND CDB.ContractFinish<="2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-04-20"))*CDB.DailyPrice WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21","2022-04-20")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-04-20")>-1');
    rows1 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish<"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish))*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-04-21" AND CDB.ContractFinish<="2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-05-21"))*CDB.DailyPrice WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21","2022-05-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-05-21")>-1');
    rows2 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish<"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish))*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-05-22" AND CDB.ContractFinish<="2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-06-21"))*CDB.DailyPrice WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22","2022-06-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-06-21")>-1');
    rows3 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish<"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish))*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-06-22" AND CDB.ContractFinish<="2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-07-22"))*CDB.DailyPrice WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22","2022-07-22")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-07-22")>-1');
    rows4 = cursor.fetchall()

    fig = px.bar(x=['فروردین','اردیبهشت','خرداد','تیر'] , y=[rows1[0][0]/1000000000,rows2[0][0]/1000000000,rows3[0][0]/1000000000,rows4[0][0]/1000000000] , 
    labels={
                     "x": "ماه",
                     "y": "فروش (میلیارد ریال)",
                     }
    )
    fig.update_layout(
    font_family="vazir",
    )
    ch = fig.to_html()
    
    labels = ['تابلوهای فعال','تابلوهای غیرفعال','تابلوهای خاموش']
    values = [4500, 2500, 1053]
    fig2 = px.pie(names=labels, values=values, hole=.3)
    fig2.update_layout(
    font_family="vazir",
    )
    ch2 = fig2.to_html()
    fig2.show()

    # cursor.execute('SELECT Bo.BoardCode , CASE WHEN MAX(CDB.ContractFinish)<"2022-08-06" THEN "EMPTY" END, MAX(CDB.ContractFinish) FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_boards AS Bo ON Bo.id =CDB.BoardID_id WHERE DATEDIFF("2022-08-06",CDB.ContractStart)>-1 GROUP BY Bo.BoardCode');
    # rowsboards = cursor.fetchall()
    # rowsboards = list(rowsboards)

    context={
        'segment': 'panel',
        'fig': ch,
        'fig2': ch2,
        # 'rowsboards':rowsboards,
    }
    return render(request, 'apps/dashboard/templates/dashboard/panel.html', context)

@login_required
def echarts(request):
    context = {'segment': 'echarts'}

    html_template = loader.get_template('apps/dashboard/templates/dashboard/echarts.html')
    return HttpResponse(html_template.render(context, request))
