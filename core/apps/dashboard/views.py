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
from datetime import datetime,date,timedelta
import plotly.express as px
import MySQLdb
import pandas as pd
from extensions.utils import jalali
from apps.formsOOH.models import Customers,Boards,Agents,ContractDetailsPerBoard, Installment,Contracts
import plotly.graph_objects as go


@login_required
def panel(request):
    conn = MySQLdb.connect(host="localhost", user="keybaanc_admin", passwd="@Code4760", db="keybaanc_db")
    cursor = conn.cursor()

    agentssales=[]
    for i in range (1,4):
        cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish<"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-04-21" AND CDB.ContractFinish<="2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-04-21" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-07-22")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-04-21","2022-07-22")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-07-22")>-1 AND CDB.AgentNameID_id ='+str(i))
        agentsale = cursor.fetchall()
        agentssales.append(agentsale[0][0])

    labels6 = ['خانم دانیالی','خانم بینایی','خانم افخمی']
    values6 = agentssales
    fig6 = px.pie(names=labels6, values=values6, hole=.3)

    fig6.update_layout(
    font_family="vazir",
    )
    ch6 = fig6.to_html()

    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish<"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-03-21" AND CDB.ContractFinish<="2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-04-20")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21","2022-04-20")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-04-20")>-1');
    rows1 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish<"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-04-21" AND CDB.ContractFinish<="2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-05-21")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21","2022-05-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-05-21")>-1');
    rows2 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish<"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-05-22" AND CDB.ContractFinish<="2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-06-21")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22","2022-06-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-06-21")>-1');
    rows3 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish<"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-06-22" AND CDB.ContractFinish<="2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-07-22")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22","2022-07-22")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-07-22")>-1');
    rows4 = cursor.fetchall()

    if(rows1[0][0]):
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
    else:
        ch = ""

    datebrd=date.today()
    datetasi = date.today()+timedelta(days = 30)
    cursor.execute('SELECT BoardCode,ContractFinish From formsOOH_contractdetailsperboard AS CDB inner join formsOOH_boards as BO ON BO.id = CDB.BoardID_id WHERE ContractStart <= "'+datebrd.strftime("%Y-%m-%d")+'" AND ContractFinish >= "'+datebrd.strftime("%Y-%m-%d")+'" AND ContractFinish <= "'+datetasi.strftime("%Y-%m-%d")+'"');
    brdfinishing = cursor.fetchall()
    aa = []
    bb = []
    for i in brdfinishing:
        for j in i:
            if (type(j) == str):
                aa.append(j)
            else:
                jj = jalali.Gregorian(j).persian_string("{}.{}.{}")
                bb.append(jj)
    print(aa)
    fig4 = go.Figure(data=[go.Table(header=dict(values=['کد تابلو', 'تاریخ پایان اکران']),
                 cells=dict(values=[aa, bb]))
                     ])
    fig4.update_layout(
    font_family="vazir",
    )
    ch4 = fig4.to_html()

    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractFinish<CURRENT_DATE THEN "0"  WHEN CDB.ContractFinish>CURRENT_DATE THEN "1" END) FROM formsOOH_contractdetailsperboard AS CDB WHERE CDB.ContractStart<CURRENT_DATE GROUP BY CDB.BoardID_id;');
    boardsstatus = cursor.fetchall()
    activebrd = 0
    deactivebrd = 0
    for i in boardsstatus:
        for j in i:
            activebrd += j
            if(j==0):
                deactivebrd+=1
    # offboards = Boards.objects.all().count() - deactivebrd - activebrd
    labels = ['تابلوهای فعال','تابلوهای غیرفعال','تابلوهای خاموش']
    values = [activebrd, deactivebrd, 0]
    fig2 = px.pie(names=labels, values=values, hole=.3)

    fig2.update_layout(
    font_family="vazir",
    )
    ch2 = fig2.to_html()

    # cursor.execute('SELECT Bo.BoardCode , CASE WHEN MAX(CDB.ContractFinish)<"2022-08-06" THEN "EMPTY" END, MAX(CDB.ContractFinish) FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_boards AS Bo ON Bo.id =CDB.BoardID_id WHERE DATEDIFF("2022-08-06",CDB.ContractStart)>-1 GROUP BY Bo.BoardCode');
    # rowsboards = cursor.fetchall()
    # rowsboards = list(rowsboards)
    xi=[]
    yi=[]
    # print(ContractDetailsPerBoard.objects.all())
    # TodayBoards = ContractDetailsPerBoard.objects.filter(ContractStart__lt='2023-01-01')
    # print(TodayBoards)
    # for i in range (365) :
    #     xi.append(jalali.Gregorian(date.today()-timedelta(days = i)).persian_string("{}.{}.{}"))
    #     yi.append(i)
    for i in range (365) :
        dateprice=date.today()-timedelta(days = i)
        xi.append(jalali.Gregorian(date.today()-timedelta(days = i)).persian_string("{}.{}.{}"))
        cursor.execute('SELECT DailyPrice From formsOOH_contractdetailsperboard AS CDB WHERE CDB.ContractStart <="'+dateprice.strftime("%Y-%m-%d")+'" AND CDB.ContractFinish >="'+dateprice.strftime("%Y-%m-%d")+'"');
        datesale = cursor.fetchall()
        # datesale = list(datesale)
        sum = 0
        for i in datesale:
            for j in i:
                sum += j

        yi.append(sum)
        # print(list(datesale[0]))
        # for i in datesale:
        #     print(list(datesale[i]))
    fig3 = px.scatter(x=xi, y=yi,
    labels={
                     "y": "فروش (ریال)",
                     }
    )
    fig3.update_layout(
    font_family="vazir",
    )
    ch3 = fig3.to_html()
    # fig3.show()


    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish<"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-03-21" AND CDB.ContractFinish<="2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-04-20")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-03-21" AND CDB.ContractFinish>"2022-04-20" THEN (TIMESTAMPDIFF(DAY,"2022-03-21","2022-04-20")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-03-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-04-20")>-1 AND CDB.AgentNameID_id ='+str(request.user.profile.id));
    rows1 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish<"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-04-21" AND CDB.ContractFinish<="2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-05-21")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-04-21" AND CDB.ContractFinish>"2022-05-21" THEN (TIMESTAMPDIFF(DAY,"2022-04-21","2022-05-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-04-21",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-05-21")>-1 AND CDB.AgentNameID_id ='+str(request.user.profile.id));
    rows2 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish<"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-05-22" AND CDB.ContractFinish<="2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-06-21")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-05-22" AND CDB.ContractFinish>"2022-06-21" THEN (TIMESTAMPDIFF(DAY,"2022-05-22","2022-06-21")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-05-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-06-21")>-1 AND CDB.AgentNameID_id ='+str(request.user.profile.id));
    rows3 = cursor.fetchall()
    cursor.execute('SELECT SUM(CASE WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish<"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart >= "2022-06-22" AND CDB.ContractFinish<="2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,CDB.ContractFinish)+1)*CDB.DailyPrice WHEN CDB.ContractStart > "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,CDB.ContractStart,"2022-07-22")+1)*CDB.DailyPrice WHEN CDB.ContractStart < "2022-06-22" AND CDB.ContractFinish>"2022-07-22" THEN (TIMESTAMPDIFF(DAY,"2022-06-22","2022-07-22")+1)*CDB.DailyPrice ELSE CDB.DailyPrice END) AS Revenue FROM formsOOH_contractdetailsperboard AS CDB INNER JOIN formsOOH_contracts AS Co ON Co.id=CDB.ContractID_id WHERE TIMESTAMPDIFF(DAY,"2022-06-22",CDB.ContractFinish)>-1 AND TIMESTAMPDIFF(DAY,CDB.ContractStart ,"2022-07-22")>-1 AND CDB.AgentNameID_id ='+str(request.user.profile.id));
    rows4 = cursor.fetchall()
    if(rows1[0][0]):
        fig5 = px.bar(x=['فروردین','اردیبهشت','خرداد','تیر'] , y=[rows1[0][0]/1000000000,rows2[0][0]/1000000000,rows3[0][0]/1000000000,rows4[0][0]/1000000000] ,
        labels={
                         "x": "ماه",
                         "y": "فروش (میلیارد ریال)",
                         }
        )
        fig5.update_layout(
        font_family="vazir",
        )
        ch5 = fig5.to_html()
    else:
        ch5 = ""

    context={
        'segment': 'panel',
        'fig': ch,
        'fig2': ch2,
        'fig3': ch3,
        'fig4': ch4,
        'fig5':ch5,
        'fig6':ch6,
        # 'rowsboards':rowsboards,
    }
    return render(request, 'apps/dashboard/templates/dashboard/panel.html', context)

@login_required
def echarts(request):
    context = {'segment': 'echarts'}

    html_template = loader.get_template('apps/dashboard/templates/dashboard/echarts.html')
    return HttpResponse(html_template.render(context, request))
