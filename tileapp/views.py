from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from tileapp.forms import pform
from tileapp.models import pmodel
from  datetime import date 
from datetime import datetime
now = date.today()
today1=date.today()
import datetime
today_date = datetime.date.today()
today = today_date.strftime("%Y-%m-%d")
def index (request):
	'''html="<html><h1>welcome<h1></html>"
	return HttpResponse(html)'''
	return render(request,'form.html')
def regload(request):
	return render(request,'form.html')
def adminhome(request):
	return render(request,'adminhome.html')
def regaction(request):
	cur=connection.cursor()
	n=request.GET['t2']
	ad=request.GET['t3']
	ph=request.GET['t4']
	em=request.GET['t5']
	sql="insert into register(name,adr,phn,em) values('%s','%s','%s','%s')" %(n,ad,ph,em)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/regload/';</script>"
	return HttpResponse(h)
def viewreg(request):
	cur=connection.cursor()
	list=[]
	s="select * from register"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'rid':row[0],'name':row[1],'adr':row[2],'phn':row[3],'em':row[4]}
	    list.append(w)
	return render(request,'viewreg.html',{'list':list})
def catload(request):
	list=vcat(request)
	return render(request,'category.html',{'list':list})
def cataction(request):
	cur=connection.cursor()
	b=request.GET['t2']
	c=request.GET['t3']
	sql="insert into tbl_category(cname,cdesc) values('%s','%s')" %(b,c)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/catload/';</script>"
	return HttpResponse(h)
def vcat(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_category"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'ccod':row[0],'cname':row[1],'cdesc':row[2]}
	    list.append(w)
	return	list
def viewcat(request):
	cur=connection.cursor()
	list=vcat(request)
	return render(request,'viewcat.html',{'list':list})
def brandload(request):
	list=vbrand(request)
	return render(request,'brand.html',{'list':list})
def brandaction(request):
	cur=connection.cursor()
	b=request.GET['t2']
	c=request.GET['t3']
	sql="insert into tbl_brand(bname,descp) values('%s','%s')" %(b,c)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/brandload/';</script>"
	return HttpResponse(h)
def vbrand(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_brand"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'bcode':row[0],'bname':row[1],'descp':row[2]}
	    list.append(w)
	return list
def viewbrand(request):
	cur=connection.cursor()
	list=vbrand(request)
	return render(request,'viewbrand.html',{'list':list})
def subcatload(request):
	cursor=connection.cursor()
	list=vcat(request)
	list1=vscat(request)
	return render(request,'subcat.html',{'list':list,'list1':list1})	
def subcataction(request):
	cur=connection.cursor()
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	sql="insert into tbl_subcat(sname,ccode,sdesc) values('%s','%s','%s')" %(b,c,d)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/subcatload/';</script>"
	return HttpResponse(h)
def vscat(request):
	cursor=connection.cursor()
	list=[]
	s="select * from tbl_subcat inner join tbl_category on tbl_category.ccod=tbl_subcat.ccode"
	cursor.execute(s)
	result=cursor.fetchall()
	for row in result:
	    w={'scode':row[0],'sname':row[1],'ccod':row[2],'sdesc':row[3],'cname':row[5]}
	    list.append(w)
	return list
def viewsubcat(request):
	cursor=connection.cursor()
	list=vscat(request)
	return render(request,'viewsubcat.html',{'list':list})	

def login(request):
	return render(request,'index.html') #rendering the template in HTTPRESPONSE

def loginaction(request):
	cursor=connection.cursor()
	p=request.POST['psw']
	e=request.POST['em']
	sql2="select * from tbl_login where uname='%s' and upass='%s'" %(e,p)
	cursor.execute(sql2)
	result=cursor.fetchall()
	if 	(cursor.rowcount) > 0:
		sql3 = "select * from tbl_login  where uname='%s' and upass='%s'" % (e, p)
		cursor.execute(sql3)
		result1 = cursor.fetchall()
		for row1 in result1:
			request.session['uid'] = row1[0]
			request.session['uname'] =row1[1] 
			request.session['utype'] = row1[3]
		if(request.session['utype']=='admin'):
			#return render(request ,'adminhome.html') 
			html="<script>alert('Logged into AdminHome ');window.location='/adminhome/';</script>"
			return HttpResponse(html)
		if(request.session['utype']=='staff'):
			return render(request ,'staffhome.html') 
			html="<script>alert('Logged into StaffHome ');window.location='/adminhom/';</script>"
			return HttpResponse(html)
		elif(request.session['utype']=='cust' ):
			return render(request ,'customerhome.html')
			html="<script>alert('Logged into User Dashboard ');window.location='/login/';</script>"
			return HttpResponse(html)
	else:
		html="<script>alert('invalid password and username ');window.location='/login/';</script>"
		return HttpResponse(html)

def logout(request):
	try:
		del request.session['uid']
		del request.session['utype']
	except:
		pass
	return HttpResponse("<script>alert('Logged out');window.location='/login/';</script>")
def vendload(request):
	list=vvend(request)
	return render(request,'vendor.html',{'list':list,'utype':request.session['utype']})
def vendaction(request):
	cur=connection.cursor()
	j=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	f=request.GET['t6']
	g=request.GET['t7']
	h=request.GET['t8']
	i=request.GET['t9']
	sql="insert into tbl_vendor(cname,oname,adr,city,dist,state,pin,em,phn) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(j,b,c,d,e,f,g,h,i)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/vendload/';</script>"
	return HttpResponse(h)
def vvend(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_vendor"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'vid':row[0],'cname':row[1],'oname':row[2],'adr':row[3],'city':row[4],'dist':row[5],'state':row[6],'pin':row[7],'em':row[8],'phn':row[9]}
	    list.append(w)
	return list
def viewvend(request):
	cur=connection.cursor()
	list=vvend(list)
	return render(request,'viewvend.html',{'list':list})
def itemload(request):
	cursor=connection.cursor()
	sql3="select * from tbl_subcat"
	cursor.execute(sql3)
	result1=cursor.fetchall()
	list=[]	
	for r in result1:
	    w1={'scode':r[0],'sname':r[1],'ccod':r[2],'sdesc':r[3]}
	    list.append(w1)
	sql="select * from tbl_category"
	cursor.execute(sql)
	result=cursor.fetchall()
	list1=[]	
	for row in result:
	    w={'ccod':row[0],'cname':row[1],'cdesc':row[2]}
	    list1.append(w)
	sql4="select * from tbl_brand"
	cursor.execute(sql4)
	result2=cursor.fetchall()
	list2=[]	
	for r1 in result2:
	    w2={'bcode':r1[0],'bname':r1[1],'descp':r1[2]}
	    list2.append(w2)
	list4=vitem(request)
	return render(request,'item.html',{'list':list,'list1':list1,'list2':list2,'list4':list4})	
def viewprod(request):
	cursor=connection.cursor()
	list4=vitem(request)
	return render(request,'viewprod.html',{'list4':list4})	
def updateitem(request):
	cur=connection.cursor()
	b=request.POST['iname']
	c=request.POST['t3']
	d=request.POST['t4']
	e=request.POST['t5']
	f=request.POST['t6']
	g=request.POST['t7']
	size=request.POST['size']
	ic=request.POST['t1']
	sql="update  tbl_item set iname='%s',bcode='%s',ccode='%s',scode='%s',desp='%s',mrp='%s',size='%s' where icode='%s'" %(b,c,d,e,f,g,size,ic)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/itemload/';</script>"
	return HttpResponse(h)
def itemaction(request):
    if request.method == "POST":
        MyProfileForm = pform(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile =pmodel()
            profile.iname = MyProfileForm.cleaned_data["iname"]
            profile.ccode =request.POST["t4"]
            profile.scode = request.POST["t5"]
            profile.bcode = request.POST["t3"]
            profile.desp = request.POST["t6"]
            profile.mrp = request.POST["t7"]
            profile.p_image = MyProfileForm.cleaned_data["p_image"]
            profile.qty = 0
            profile.size =request.POST["size"]
            profile.save()
            html = "<script>alert('successfully added! ');window.location='/itemload/';</script>"
            saved = True
	else:
		MyProfileForm = pform()
	return HttpResponse(html)
def vitem(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_item"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'icode':row[0],'iname':row[1],'bcode':row[2],'ccode':row[3],'scode':row[4],'desp':row[5],'mrp':row[6],'qty':row[7],'p_image':row[8],'size':row[9]}
	    list.append(w)
	return	list
def viewitem(request):
	cur=connection.cursor()
	list=vitem(request)
	return render(request,'viewitem.html',{'list':list})
def staffload(request):
	list=vstaff(request)
	return render(request,'staff.html',{'list':list})
def staffaction(request):
	cur=connection.cursor()
	a=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	f=request.GET['t6']
	g=request.GET['t7']
	h=request.GET['t8']
	i=request.GET['t9']
	p=request.GET['t10']
	jdate=request.GET['t12']
	sql="insert into tbl_staff(sname,shname,sstreet,scity,sdist,spin,sstate,sphn,sem,jdate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(a,b,c,d,e,f,g,h,i,jdate)
	cur.execute(sql)
	sq="select max(staffid)  from tbl_staff"
	cur.execute(sq)
	result=cur.fetchall()
	list=[]
	for row in result:
		id=row[0]
	emailsql="insert into tbl_login(uid,uname,upass,utype) values('%s','%s','%s','%s')" %(id,i,p,'staff')
	cur.execute(emailsql)
	h="<script>alert('successfully inserted');window.location='/staffload/';</script>"
	return HttpResponse(h)
def vstaff(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_staff"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'staffid':row[0],'sname':row[1],'shname':row[2],'sstreet':row[3],'scity':row[4],'sdist':row[5],'spin':row[6],'sstate':row[7],'sphn':row[8],'sem':row[9],'jdate':row[10]}
	    list.append(w)
	return list
def viewstaff(request):
	cur=connection.cursor()
	list=vstaff(request)
	return render(request,'viewstaff.html',{'list':list})
def staffreport(request):	
	cur=connection.cursor()
	list=[]
	cursor = connection.cursor()
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		s="select  * from  tbl_staff   where jdate between '%s' and '%s'"%(d1,d2)
	else:
		s="select * from tbl_staff"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'staffid':row[0],'sname':row[1],'shname':row[2],'sstreet':row[3],'scity':row[4],'sdist':row[5],'spin':row[6],'sstate':row[7],'sphn':row[8],'sem':row[9],'jdate':row[10]}
	    list.append(w)
	return render(request,'staffreport.html',{'list':list})
def custload(request):
	return render(request,'customer.html')
def custaction(request):
	cur=connection.cursor()
	a=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	f=request.GET['t6']
	g=request.GET['t7']
	h=request.GET['t8']
	i=request.GET['t9']
	p=request.GET['t10']	
	sql="insert into tbl_customer(cname,chname,cstreet,ccity,cdist,cpin,cstate,cphn,cem,rdate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(a,b,c,d,e,f,g,h,i,today)
	cur.execute(sql)
	sq="select max(cid) as uid from tbl_customer"
	cur.execute(sq)
	result=cur.fetchall()
	list=[]
	for row in result:
		id=row[0]
	emailsql="insert into tbl_login(uid,uname,upass,utype) values('%s','%s','%s','%s')" %(id,i,p,'cust')
	cur.execute(emailsql)
	h="<script>alert('successfully inserted');window.location='/home/';</script>"
	return HttpResponse(h)

def payload(request):
	return render(request,'pay.html')
def payaction(request):
	cur=connection.cursor()
	a=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	sql="insert into tbl_pay(chname,cno,cvv,cdate,amt) values('%s','%s','%s','%s','%s')" %(a,b,c,d,e)
	cur.execute(sql)
	h="<script>alert('successfully inserted');window.location='/payload/';</script>"
	return HttpResponse(h)
def viewpay(request):
	cur=connection.cursor()
	list=[]
	s="select * from tbl_pay"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'payid':row[0],'chname':row[1],'cno':row[2],'cvv':row[3],'cdate':row[4],'amt':row[5],'oid':row[6]}
	    list.append(w)
	return render(request,'viewpay.html',{'list':list})
	
def delbrnd(request):
    cursor=connection.cursor()
    n=request.GET['n']
	
    sql="delete from tbl_brand where bcode='%s'"%(n)
    cursor.execute(sql)
    h="<script>alert('success');window.location='/brandload/';</script>"
    return HttpResponse(h)	
def delvendr(request):
	cursor=connection.cursor()
	n=request.GET['n']
	
	sql="delete from tbl_vendor where vid='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('success');window.location='/addvendor/';</script>"

	return HttpResponse(h)	
def delcat(request):
	cursor=connection.cursor()
	n=request.GET['n']
	
	sql="delete from tbl_category where ccod='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('success');window.location='/catload/';</script>"

	return HttpResponse(h)	
def delsubcat(request):
	cursor=connection.cursor()
	n=request.GET['n']
	
	sql="delete from tbl_subcat where scode='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('success');window.location='/subcatload/';</script>"

	return HttpResponse(h)
def delprod(request):
	cursor=connection.cursor()
	n=request.GET['n']
	
	sql="delete from tbl_item where icode='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('success');window.location='/itemload/';</script>"

	return HttpResponse(h)	
def purchaseaction(request):
    cursor=connection.cursor()
    st=request.session['uid']
    dn=request.GET['dnm']
    pd=request.GET['pdt']
    sql="insert into tbl_pmaster(staff_id,dist_id,pdate,tamt) values('%s','%s','%s','%s')"%(st,dn,pd,'0')
    cursor.execute(sql)
    h="<script>window.location='/purchase/';</script>"
    return HttpResponse(h)
def  purchase(request):
	cursor = connection.cursor()
	if(request.session['utype']=='admin'):
		sql2="select tbl_pmaster.pmid,tbl_pmaster.pdate,tbl_pmaster.tamt,tbl_vendor.cname from tbl_pmaster  inner join tbl_vendor on tbl_pmaster.dist_id=tbl_vendor.vid "
    
	elif(request.session['utype']=='staff'):
		sql2="select tbl_pmaster.pmid,tbl_pmaster.pdate,tbl_pmaster.tamt,tbl_vendor.cname from tbl_pmaster  inner join tbl_vendor on tbl_pmaster.dist_id=tbl_vendor.vid where tbl_pmaster.staff_id='%s'"%(request.session['uid'])
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {'pmid' : row[0],'pdate': row[1],'tamt':row[2],'dist_name':row[3]}
		list.append(w)
	list2=vvend(request)
	return render(request,'purchase.html', {'list1': list,'list2':list2,'utype':request.session['utype']})
def  pchild(request):
    cursor = connection.cursor()
    pmid=request.GET['pid']
    sql2="select tbl_pchild.*,tbl_item.iname from tbl_pchild inner join tbl_item on tbl_pchild.icode=tbl_item.icode where pmid='%s'"%(pmid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    for row in result:
        w = {'pchild_id' : row[0],'pmid': row[1],'book_id':row[2],'tqty':row[3],'uprice':row[4],'tamt':row[5],'book_name':row[6]}
        list.append(w)
    list2=vitem(request)
    return render(request,'purchild.html', {'list1': list,'list2':list2,'pmid':pmid,'utype':request.session['utype']})
def  pchild1(request):
    cursor = connection.cursor()
    pmid=request.GET['pid']
    sql2="select tbl_pchild.*,tbl_item.iname from tbl_pchild inner join tbl_item on tbl_pchild.icode=tbl_item.icode where pmid='%s'"%(pmid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    for row in result:
        w = {'pchild_id' : row[0],'pmid': row[1],'book_id':row[2],'tqty':row[3],'uprice':row[4],'tamt':row[5],'book_name':row[6]}
        list.append(w)
    list2=vitem(request)
    return render(request,'purchild1.html', {'list1': list,'list2':list2,'pmid':pmid,'utype':request.session['utype']})
def purchildaction(request):
    cursor=connection.cursor()
    pmid=request.GET['t0']
    bid=request.GET['bid']
    qty=request.GET['tqt']
    uamt=request.GET['utpr']
    tamt=int(qty)*int(uamt)
    sql="insert into tbl_pchild(pmid,icode,tqty,uprice,tamt) values('%s','%s','%s','%s','%s')"%(pmid,bid,qty,uamt,tamt)
    cursor.execute(sql)
    sql2="select tamt from tbl_pmaster where pmid='%s'"%(pmid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    for row in result:
        pm=row[0]
	pmn=int(pm)+tamt
    sql4="select qty from tbl_item where icode='%s'"%(bid)
    cursor.execute(sql4)
    result3=cursor.fetchall()
    for row3 in result3:
        bqty1=int(row3[0])
    bqty=bqty1+int(qty)
    sql3="update tbl_pmaster set tamt='%s'  where pmid='%s'"%(pmn,pmid)
    cursor.execute(sql3)
    sql5="update tbl_item set qty='%s'  where icode='%s'"%(bqty,bid)
    cursor.execute(sql5)
    h="<script>window.location='/pchild?pid=%s';</script>"%(pmid)
    return HttpResponse(h)
def delpchild(request):
    cursor=connection.cursor()
    id=request.GET['id']
    sql2="select tamt,pmid,tqty,icode from tbl_pchild where pchild_id='%s'"%(id)
    cursor.execute(sql2)
    result=cursor.fetchall()
    for row in result:
        ctamt=row[0]
        pmid=row[1]
        tqty=int(row[2])
        bid=row[3]
    sql3="select tamt from tbl_pmaster where pmid='%s'"%(pmid)
    cursor.execute(sql3)
    result1=cursor.fetchall()
    for row1 in result1:
        ptamt=row1[0]
    amt=int(ptamt)-int(ctamt)
    sql3="update tbl_pmaster set tamt='%s'  where pmid='%s'"%(amt,pmid)
    cursor.execute(sql3)
    sql="delete from tbl_pchild where pchild_id='%s'"%(id)
    cursor.execute(sql)
    sql4="select qty from tbl_item where icode='%s'"%(bid)
    cursor.execute(sql4)
    result3=cursor.fetchall()
    for row3 in result3:
        bqty1=int(row3[0])
    bqty=bqty1-tqty
    sql5="update tbl_item set qty='%s'  where icode='%s'"%(bqty,bid)
    cursor.execute(sql5)
    h="<script>window.location='/pchild?pid=%s';</script>"%(pmid)
    return HttpResponse(h)			
	
def vproduct(request):
    cursor = connection.cursor()
    if (request.method == 'GET' and 'srh' in request.GET):
        se=request.GET['srh']
        p="select tbl_item.icode,tbl_item.iname,tbl_item.desp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_category.cname,tbl_subcat.sname,tbl_brand.bname,tbl_item.size  from tbl_item  inner join tbl_category on tbl_item.ccode=tbl_category.ccod inner join tbl_subcat on tbl_item.scode=tbl_subcat.scode inner join tbl_brand on  tbl_item.bcode=tbl_brand.bcode  where tbl_item.icode like '%%%s%%' or  tbl_item.iname like '%%%s%%' or  tbl_category.cname like '%%%s%%' or  tbl_subcat.sname like '%%%s%%' or tbl_brand.bname like '%%%s%%'" %(se,se,se,se,se)
    else:
        p="select tbl_item.icode,tbl_item.iname,tbl_item.desp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_category.cname,tbl_subcat.sname,tbl_brand.bname,tbl_item.size  from tbl_item  inner join tbl_category on tbl_item.ccode=tbl_category.ccod inner join tbl_subcat on tbl_item.scode=tbl_subcat.scode inner join tbl_brand on  tbl_item.bcode=tbl_brand.bcode "# where tbl_item.icode='%s'" %(request.GET['id'])
    cursor.execute(p)
    re1=cursor.fetchall()
    pdt=[]
    for sy3 in re1:
        y3 = {'pcode':sy3[0],'pname' : sy3[1],'descp' : sy3[2],'mrp' : sy3[3],'qty' : sy3[4],'p_image':sy3[5],'ccode' : sy3[6],'sccode' : sy3[7],'bcode' : sy3[8],'size':sy3[9]}
        pdt.append(y3)
    return render(request,'vproducts.html', {'list2':pdt})
  
def vproduct1(request):
    cursor = connection.cursor()
    sql2="select tbl_item.icode,tbl_item.iname,tbl_item.descp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_category.cname,tbl_subcat.sname,tbl_brand.bname  from tbl_item  inner join tbl_category on tbl_item.ccode=tbl_category.ccod inner join tbl_subcat on tbl_item.scode=tbl_subcat.scode inner join tbl_brand on  tbl_item.bcode=tbl_brand.bcode  order by tbl_item.icode desc limit 6"
    cursor.execute(sql2)
    re1=cursor.fetchall()
    pdt=[]
    for sy3 in re1:
        y3 ={'pcode':sy3[0],'pname' : sy3[1],'descp' : sy3[2],'mrp' : sy3[3],'qty' : sy3[4],'p_image':sy3[5],'ccode' : sy3[6],'sccode' : sy3[7],'bcode' : sy3[8]}
        pdt.append(y3) 
    return pdt
def pdetails(request):
	cursor = connection.cursor()
	p="select tbl_item.icode,tbl_item.iname,tbl_item.desp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_category.cname,tbl_subcat.sname,tbl_brand.bname,tbl_item.size  from tbl_item  inner join tbl_category on tbl_item.ccode=tbl_category.ccod inner join tbl_subcat on tbl_item.scode=tbl_subcat.scode inner join tbl_brand on  tbl_item.bcode=tbl_brand.bcode  where tbl_item.icode='%s'" %(request.GET['id'])
	cursor.execute(p)
	re1=cursor.fetchall()
	pdt=[]
	for sy3 in re1:
		y3 = {'pcode':sy3[0],'pname' : sy3[1],'descp' : sy3[2],'mrp' : sy3[3],'qty' : str(sy3[4]),'p_image':sy3[5],'ccode' : sy3[6],'sccode' : sy3[7],'bcode' : sy3[8],'size' : sy3[9]}
		pdt.append(y3)
	return render(request,'pdetail.html', {'list2':pdt})
def editprod(request):
	cursor = connection.cursor()
	p="select tbl_item.icode,tbl_item.iname,tbl_item.desp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_category.cname,tbl_subcat.sname,tbl_brand.bname,tbl_item.size ,tbl_item.ccode,tbl_item.scode,tbl_item.bcode from tbl_item  inner join tbl_category on tbl_item.ccode=tbl_category.ccod inner join tbl_subcat on tbl_item.scode=tbl_subcat.scode inner join tbl_brand on  tbl_item.bcode=tbl_brand.bcode  where tbl_item.icode='%s'" %(request.GET['n'])
	cursor.execute(p)
	re1=cursor.fetchall()
	pdt=[]
	for sy3 in re1:
		y3 = {'pcode':sy3[0],'pname' : sy3[1],'descp' : sy3[2],'mrp' : sy3[3],'qty' : str(sy3[4]),'p_image':sy3[5],'cname' : sy3[6],'sname' : sy3[7],'bname' : sy3[8],'size' : sy3[9],'ccode' : sy3[10],'sccode' : sy3[11],'bcode' : sy3[12]}
		pdt.append(y3)
	list=vcat(request)
	list1=vscat(request)
	list2=vbrand(request)
	return render(request,'editprod.html', {'list':list,'list1':list1,'list2':list2,'list4':pdt})
def custhome(request):
    list=vproduct1(request) 
    #list1=vcat(request)
    return render(request,'custhome.html', {'pro': list})#,'cat':list1})
def cart(request):
    cursor=connection.cursor()
    bi=request.GET['bi']
    qty=request.GET['qty']
    uid=request.session['uid']
    sql2="select * from tbl_cart where icode='%s' and uid='%s'"%(bi,uid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    if(cursor.rowcount>0):
        h="<script>alert('already exist in cart');window.location='/custhome/';</script>"
    else:  
        sql1="insert into tbl_cart(icode,uid,cqty) values('%s','%s','%s')" %(bi,uid,qty)
        cursor.execute(sql1)
        h="<script>window.location='/vcart/';</script>"
    return HttpResponse(h)

def vcart(request):
    cursor = connection.cursor()
    uid=request.session['uid']	
    p="select tbl_item.icode,tbl_item.iname,tbl_item.desp,tbl_item.mrp,tbl_item.qty,tbl_item.p_image,tbl_cart.cqty,tbl_cart.cid from tbl_item INNER JOIN tbl_cart ON tbl_cart.icode=tbl_item.icode where tbl_cart.uid='%s'" %(uid)
    cursor.execute(p)
	#return HttpResponse(p)
    re1=cursor.fetchall()
    pdt=[]
    total=0
    for sy3 in re1:
        cqty=int(sy3[6])
        price=int(sy3[3])
        ttt=(cqty*price)
        total=total+ttt
        y3 = {'pcode':sy3[0],'pname' : sy3[1],'descp' : sy3[2],'mrp' : sy3[3],'qty' : sy3[4],'p_image':sy3[5],'cqty' : sy3[6],'cid':sy3[7],'ttt':ttt}
        pdt.append(y3)
    return render(request,'vcart.html', {'list2':pdt,'total':total,'date':today})
def delcart(request):
    cursor=connection.cursor()
    id=request.GET['id']
    sql="delete from tbl_cart where cid='%s'"%(id)
    cursor.execute(sql)
    h="<script>window.location='/vcart/';</script>"
    return HttpResponse(h)
def buyaction(request):
    cursor=connection.cursor()
    uid=request.session['uid'];
    cardno=request.GET['vnm'];
    cvv=request.GET['bnm'];
    edate=request.GET['edate'];
    tamount=request.GET['stnm'];
    odate=today
    s1="select sum(cqty) as cnt from tbl_cart where uid='%s'"%(uid)
    cursor.execute(s1)
    result=cursor.fetchall()
    tamt=0
    for row in result:
        tqty=row[0]
    #--------------------------------------------------
    sql="insert into tbl_order(uid,tqty,tamt,ostatus,odate) values ('%s','%s','%s','%s','%s')"%(uid,tqty,'0','pending',odate)
    cursor.execute(sql)
    #-------------------------------------
    ss="select max(oid) as oid from tbl_order"
    cursor.execute(ss)
    result1=cursor.fetchall()
    for c1 in result1:
        oid=c1[0]
    #---------------------------------------------------
    s="select * from tbl_cart where uid=%s"%(uid)
    cursor.execute(s)
    result2=cursor.fetchall()
    for r1 in result2:
        pcode=r1[1];
        qt=int(r1[3])
        sg="SELECT mrp,qty from tbl_item where icode='%s'" %(pcode)
        cursor.execute(sg)
        result3=cursor.fetchall()
        for m1 in result3:
                pqty=int(m1[1])
                s=(int(m1[0])*qt)
                tamt=tamt+s
                stqty=pqty-qt
        sql1="insert into tbl_orderc(oid,icode,qty) values('%s','%s','%s')"%(oid,pcode,qt)
        cursor.execute(sql1)
        sqle="update tbl_item set qty='%s' where icode='%s'" %(stqty,pcode)
        cursor.execute(sqle)
        sql2="delete from tbl_cart where uid='%s' and icode='%s'"%(uid,pcode)
        cursor.execute(sql2)
    #------------------------------------------------
    s2="update tbl_order set tamt='%s' where oid='%s'"%(tamt,oid)
    cursor.execute(s2)
    sql3="insert into tbl_pay(oid,uid,cardno,cvv,edate)values('%s','%s','%s','%s','%s')"%(oid,uid,cardno,cvv,edate)
    cursor.execute(sql3)
    h="<script> alert('success'); window.location='/myorder/'; </script>"
    return HttpResponse(h)   
def myorder(request):
    cursor = connection.cursor()
    a=request.session['uid']
    sql2="select tbl_order.ostatus,tbl_item.iname,tbl_orderc.qty,tbl_item.mrp,tbl_item.p_image from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode where tbl_order.uid='%s' order by tbl_order.oid desc"%(a)
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    total=0
    for row in result:
        cqty=int(row[2])
        #return HttpResponse(cqty)
        price=int(row[3])
        ttt=(cqty*price)
        total=total+ttt
        w = {'ostatus' : row[0],'pname': row[1],'qty' : row[2],'mrp': row[3],'p_image' : row[4],'ttt':ttt}
        list.append(w)   
    #list1=vcat(request)
    return render(request,'myorders.html', {'book': list,'total':total,'date':today})    
def buy(request):
	cursor = connection.cursor()
	uid=request.session['uid']	
	p="select tbl_cart.pcode,tbl_item.iname,tbl_item.mrp from tbl_item INNER JOIN tbl_cart ON tbl_cart.pcode=tbl_item.icode where uid='%s'" %(uid)
	cursor.execute(p)
	re1=cursor.fetchall()
	pdt=[]
	for sy3 in re1:
		y3 = {'pcode':sy3[0],'pname':sy3[1],'mrp' : sy3[2]}
		pdt.append(y3)
	return render(request,'buy.html', {'list2':pdt})
def porder1(request):
	cursor = connection.cursor()
	a=request.session['uid']
	sql2="select tbl_order.oid,tbl_item.iname,tbl_orderc.qty,tbl_item.mrp,tbl_item.p_image,tbl_customer.cname,tbl_customer.cphn,tbl_customer.chname,tbl_customer.ccity,tbl_customer.cdist,tbl_customer.cpin from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode inner join tbl_customer on tbl_customer.cid=tbl_order.uid where tbl_order.ostatus='pending' order by tbl_order.oid desc";
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {'oid' : row[0],'pname': row[1],'qty' : row[2],'mrp': row[3],'p_image' : row[4],'cname' : row[5],'cphno': row[6],'chouse' : row[7],'ccity':row[8],'cdist' : row[9],'cpin':row[10]}
		list.append(w)
	return list
def porder(request):
	list=porder1(request)
	list1=vstaff(request)
	return render(request,'porder.html', {'order': list,'staff':list1})    
    
def adminhome(request):
	return render(request,'adminhome.html')
def assign(request):
	cursor = connection.cursor()
	oid=request.GET['oid'];
	st=request.GET['st'];
	sql="insert into tbl_assign(oid,stid)values('%s','%s')"%(oid,st)
	cursor.execute(sql)
	sql1="update tbl_order set ostatus='Assigned' WHERE oid='%s'"%(oid)
	cursor.execute(sql1)
	h="<script> alert('assigned'); window.location='/adminhome/'; </script>"
	return HttpResponse(h)
def vorders(request):
    cursor = connection.cursor()
    a=request.session['uid']
    sql2="select tbl_order.ostatus,tbl_item.iname,tbl_orderc.qty,tbl_item.mrp,tbl_item.p_image from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode order by tbl_order.oid desc"
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    total=0
    for row in result:
        cqty=int(row[2])
        #return HttpResponse(cqty)
        price=int(row[3])
        ttt=(cqty*price)
        total=total+ttt
        w = {'ostatus' : row[0],'book_name': row[1],'qty' : row[2],'book_price': row[3],'book_image' : row[4],'ttt':ttt}
        list.append(w)   
    
    return render(request,'vorders.html', {'book': list,'total':total,'date':today})
def orderreport(request):
	cursor = connection.cursor()
	a=request.session['uid']
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select tbl_item.iname,tbl_orderc.qty,tbl_order.odate,tbl_item.mrp,tbl_item.p_image,tbl_order.ostatus,tbl_staff.sname,tbl_customer.cname,tbl_customer.cphn,tbl_customer.cphn from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode inner join tbl_customer   on tbl_customer.cid=tbl_order.uid  inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join tbl_staff  on tbl_staff.staffid=tbl_assign.stid where odate between '%s' and '%s'   order by tbl_order.oid desc"%(d1,d2)
	
	elif (request.method == 'GET' and 'dev' in request.GET):
		sql2="select tbl_item.iname,tbl_orderc.qty,tbl_order.odate,tbl_item.mrp,tbl_item.p_image,tbl_order.ostatus,tbl_staff.sname,tbl_customer.cname,tbl_customer.cphn,tbl_customer.cphn from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode inner join tbl_customer   on tbl_customer.cid=tbl_order.uid  inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join tbl_staff  on tbl_staff.staffid=tbl_assign.stid where ostatus='Delivered'   order by tbl_order.oid desc"
	else:
		sql2="select tbl_item.iname,tbl_orderc.qty,tbl_order.odate,tbl_item.mrp,tbl_item.p_image,tbl_order.ostatus,tbl_staff.sname,tbl_customer.cname,tbl_customer.cphn,tbl_customer.cphn from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode inner join tbl_customer   on tbl_customer.cid=tbl_order.uid  inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join tbl_staff  on tbl_staff.staffid=tbl_assign.stid  order by tbl_order.oid desc"
	
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		price=int(row[1])
		cqty=int(row[3])
		ttt=(cqty*price)
		w = {'book_name' : row[0],'qty': row[1],'odate' : row[2],'book_price': row[3],'book_image' : row[4],'ostatus' : row[5],'staff_name': row[6],'cname' : row[7],'cpho': row[8],'cemail':row[9],'total':ttt}#,'cdist' : row[10],'cpin':row[11]}
		list.append(w)
	if (request.method == 'GET' and 'dev' in request.GET):
		return render(request,'dreports.html', {'order': list})
	else:
		return render(request,'reports.html', {'order': list})
 
def aorders(request):
	cursor = connection.cursor()
	uid=request.session['uid']
	sql2="select tbl_order.oid,tbl_order.ostatus,tbl_item.iname,tbl_orderc.qty,tbl_item.mrp,tbl_customer.cname,tbl_customer.cphn,tbl_customer.chname,tbl_customer.ccity,tbl_customer.cdist,tbl_customer.cpin from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode inner join tbl_customer on tbl_customer.cid=tbl_order.uid inner join tbl_assign on tbl_assign.oid=tbl_order.oid where tbl_assign.stid='%s' order by tbl_order.oid desc"%(uid)	
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {'oid' : row[0],'ostatus':row[1],'book_name': row[2],'qty' : row[3],'book_price': row[4],'cname' : row[5],'cphno': row[6],'chouse' : row[7],'ccity':row[8],'cdist' : row[9],'cpin':row[10]}
		list.append(w)
	return render(request,'aorders.html', {'order': list})
def status(request):
	cursor = connection.cursor()
	oid=request.GET['oid']
	sts=request.GET['s']
	sql="update tbl_order set ostatus='%s' WHERE oid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>  window.location='/aorders/'; </script>"
	return HttpResponse(h)
def sprofile(request):
	cur = connection.cursor()
	sql2="select * from tbl_staff where staffid='%s'"%(request.session['uid'])
	cur.execute(sql2)
	result=cur.fetchall()
	list=[]
	for row in result:
		w={'staffid':row[0],'sname':row[1],'shname':row[2],'sstreet':row[3],'scity':row[4],'sdist':row[5],'spin':row[6],'sstate':row[7],'sphn':row[8],'sem':row[9],'jdate':row[10]}
		list.append(w)
	return render(request,'prstaff.html', {'list': list})
def staffhome(request):
    list=sprofile(request)
    return render(request,'staffhom.html', {'staff': list})
def updatesprofile(request):
	cursor=connection.cursor()
	a=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	f=request.GET['t6']
	g=request.GET['t7']
	h=request.GET['t8']
	i=request.GET['t9']
	p=request.GET['t10']
	sid=request.session['uid']
	sql="update  tbl_staff set sname='%s',shname='%s',sstreet='%s',scity='%s',sdist='%s',spin='%s',sstate='%s',sphn='%s',sem='%s' where staffid='%s'"%(a,b,c,d,e,f,g,h,i,sid)
	cursor.execute(sql)
	sql1="update tbl_login set uname='%s',upass='%s' where uid='%s' and utype='staff'" %(e,p,sid)
	cursor.execute(sql1)
	h="<script>window.location='/sprofile/';</script>"
	return HttpResponse(h)
def  profile(request):
	cursor = connection.cursor()
	sql2="select * from tbl_customer where cid='%s'"%(request.session['uid'])

	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
	    w={'cid':row[0],'cname':row[1],'chname':row[2],'cstreet':row[3],'ccity':row[4],'cdist':row[5],'cpin':row[6],'cstate':row[7],'cphn':row[8],'cem':row[9],'rdate':row[10]}
	    list.append(w)
	return render(request,'profile.html', {'list': list}) 
def cupdateaction(request):
	cursor=connection.cursor()
	a=request.GET['t1']
	b=request.GET['t2']
	c=request.GET['t3']
	d=request.GET['t4']
	e=request.GET['t5']
	f=request.GET['t6']
	g=request.GET['t7']
	h=request.GET['t8']
	i=request.GET['t9']
	p=request.GET['t10']	
	sql="update tbl_customer set cname='%s',chname='%s',cstreet='%s',ccity='%s',cdist='%s',cpin='%s',cstate='%s',cphn='%s',cem='%s' where cid='%s'"%(a,b,c,d,e,f,g,h,i,request.session['uid'])
	cursor.execute(sql)
	sql1="update  tbl_login set uname='%s',upass='%s' where uid='%s' and utype='cust' "%(e,p,request.session['uid'])
	cursor.execute(sql1)
	h="<script>alert('sucessfully updated');window.location='/profile/';</script>"
	return HttpResponse(h)	
'''def staffreport(request):
	list1=vstaff(request)
	return render(request,'staffreport.html', {'list':list1})  '''  			
			
def salereport(request):
	cursor = connection.cursor()
	a=request.session['uid']
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select tbl_item.iname,tbl_orderc.qty,tbl_order.odate,tbl_item.mrp,tbl_item.p_image from  tbl_orderc inner join tbl_order on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode  where tbl_order.odate between '%s' and '%s'   order by tbl_order.oid desc"%(d1,d2)
	else:
		sql2="select tbl_item.iname,tbl_orderc.qty,tbl_order.odate,tbl_item.mrp,tbl_item.p_image from  tbl_orderc inner join tbl_order on tbl_orderc.oid=tbl_order.oid inner join tbl_item on tbl_item.icode=tbl_orderc.icode     order by tbl_order.oid desc"
	
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		price=int(row[3])
		cqty=int(row[1])
		ttt=(cqty*price)
		w = {'book_name' : row[0],'qty': row[1],'odate' : row[2],'book_price': row[3],'book_image' : row[4],'total':ttt}
		list.append(w)
	return render(request,'salereports.html', {'list':list})  
def venreport(request):
	list1=vvend(request)
	return render(request,'venreport.html', {'list':list1}) 	
def purreport(request):
	cursor = connection.cursor()
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select tbl_pchild.icode,tbl_pchild.tqty,tbl_pchild.uprice,tbl_pchild.tamt,tbl_pmaster.pdate from tbl_pchild  inner join tbl_pmaster   on tbl_pmaster.pmid=tbl_pchild.pmid  where tbl_pmaster.pdate between '%s' and '%s'"%(d1,d2)
	else:
		sql2="select tbl_pchild.icode,tbl_pchild.tqty,tbl_pchild.uprice,tbl_pchild.tamt,tbl_pmaster.pdate from tbl_pchild  inner join tbl_pmaster   on tbl_pmaster.pmid=tbl_pchild.pmid  "
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		price=int(row[1])
		cqty=int(row[3])
		ttt=(cqty*price)
		w = {'icode' : row[0],'pqty': row[1],'pamt' : row[2],'tamt': row[3],'pdate':row[4]}
		list.append(w)
	return render(request,'purreports.html', {'list':list}) 	
def viewcust(request):
	cur=connection.cursor()
	list=[]
	cursor = connection.cursor()
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		s="select  * from  tbl_customer   where rdate between '%s' and '%s'"%(d1,d2)
	else:
		s="select * from tbl_customer"
	cur.execute(s)
	result=cur.fetchall()
	for row in result:
	    w={'cid':row[0],'cname':row[1],'chname':row[2],'cstreet':row[3],'ccity':row[4],'cdist':row[5],'cpin':row[6],'cstate':row[7],'cphn':row[8],'cem':row[9],'rdate':row[10]}
	    list.append(w)
	return render(request,'viewcust.html',{'list':list})		
		