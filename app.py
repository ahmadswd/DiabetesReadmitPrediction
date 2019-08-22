from flask import Flask,jsonify
from flask_cors import CORS
from flask import render_template
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
import pymongo
import uuid
import json
from bson import ObjectId
import numpy as np
import pickle


DEBUG = True

application = Flask(__name__)
application.config.from_object(__name__)

incoming_data = []

CORS(application, resources={r'/*': {'origins': '*'}})
@application.route('/index',methods=['GET', 'POST'])
@application.route('/',methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
      post_data = request.get_json()
      hours = post_data.get('hrs')
      prolab = post_data.get('lab')
      prod = post_data.get('pro')
      medic = post_data.get('med')
      outpat = post_data.get('out')
      emerg = post_data.get('eme')
      inpat = post_data.get('inp')
      diag = post_data.get('dig')

      adt = post_data.get('adt')
      ads = post_data.get('ads')
      did = post_data.get('did')
      mes = post_data.get('mes')
      pay = post_data.get('pay')
      rac = post_data.get('rac')
      gen = post_data.get('gen')
      agr = post_data.get('agr')
      wem = post_data.get('wem')
      gls = post_data.get('gls')
      a1c = post_data.get('a1c')
      com = post_data.get('com')
      met = post_data.get('met')
      rep = post_data.get('rep')
      nat = post_data.get('nat')
      chl = post_data.get('chl')
      glim = post_data.get('glim')
      ace = post_data.get('ace')
      glip = post_data.get('glip')
      glyb = post_data.get('glyb')
      tol = post_data.get('tol')
      pio = post_data.get('pio')
      ros = post_data.get('ros')
      aca = post_data.get('aca')
      mmg = post_data.get('mmg')
      tro = post_data.get('tro')
      ins = post_data.get('ins')
      gly = post_data.get('gly')
      gli = post_data.get('gli')
      glp = post_data.get('glp')
      mer = post_data.get('mer')
         #incoming_data.applicationend(hours)
         # incoming_data.applicationend(prolab)
         # incoming_data.applicationend(prod)
         # ti=post_data.get('title')
         # print(type(hours))
         # print(prolab) 
         # print(prod)
         # print(medic)
         # print(outpat)
         # print(emerg)
         # print(inpat)
         # print(diag)
         # print(adt)
         # print(ads)
         # print(did)
         # print(mes)
         # print(pay)
         # print(rac)
         # print(gen)
         # print(agr)
         # print(wem)
         # print(gls)
         # print(a1c)
         # print(com)
         # print(met)
         # print(rep)
         # print(nat)
         # print(chl)
         # print(glim)
         # print(ace)
         # print(glip)
         # print(glyb)
         # print(tol)
         # print(pio)
         # print(ros)
         # print(aca)
         # print(mmg)
         # print(tro)
         # print(ins)
         # print(gly)
         # print(gli)
         # print(glp)
         # print(type(mer))
      
      race ={'Asian':0,'Caucasian':0,'Hispanic':0,'Other':0,'UNK':0}
      gender ={'Male':0,'Unknown/Invalid':0}
      if gen == 'Male':
         gender['Male']=1
      else:
         gender['Unknown/Invalid']=1
      glue ={'> 300':0,'None':0,'Norm':0}
      glue[gls]=1

      aa1c ={'> 8':0,'None':0,'Norm':0}
      aa1c[a1c]=1

      mett ={'No':0,'Steady':0,'Up':0}
      repp ={'No':0,'Steady':0,'Up':0}
      natt ={'No':0,'Steady':0,'Up':0}
      chll ={'No':0,'Steady':0,'Up':0}
      glimm ={'No':0,'Steady':0,'Up':0}
      acee=[0]
      glipp={'No':0,'Steady':0,'Up':0}
      glypp ={'No':0,'Steady':0,'Up':0}
      toll=[0]
      pioo={'No':0,'Steady':0,'Up':0}
      ross ={'No':0,'Steady':0,'Up':0}
      acaa ={'No':0,'Steady':0,'Up':0}
      mmgg={'No':0,'Steady':0,'Up':0}
      tol = [0]
      troo ={'Steady':0,'Up':0}
      inss ={'No':0,'Steady':0,'Up':0}
      glyy ={'No':0,'Steady':0,'Up':0}
      glipz = [0]
      glii =[0]
      megg = [0]
      merr=[0]
      comm = []
      if com == 'Yes':
         comm=[1]
      else:
         comm=[0]
      
      payer = {'CH':0,'CM':0,'CP':0,'DM':0,'FR':0,'HM':0,'MC':0,'MD':0,'MP':0,'OG':0,'OT':0,'PO':0,'SI':0,'SP':0,'UN':0,'UNK':0,'WC':0}
      adtt = {'Urgent':0,'Elective':0,'Newborn':0,'Not Available':0,'Null':0,'Trauma Center':0,'Not Mapped':0}
      disc = {'Neonate discharged to another hospital for neonatal aftercare':0,
      'Still patient or expected to return for outpatient services':0,
      'Discharged/transferred within this institution to Medicare approved swing bed':0,
      'Discharged/transferred/referred another institution for outpatient services':0,
      'Discharged/transferred/referred to this institution for outpatient services':0,
      'NULL':0,
      'Discharged/transferred to another short term hospital':0,
      'Discharged/transferred to another rehab fac including rehab units of a hospital':0,
      'Discharged/transferred to a long term care hospital'
      'Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare':0,
      'Not Mapped':0,
      'Discharged/transferred to a federal health care facility':0,
      'Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital':0,
      'Discharged/transferred to SNF':0,
      'Discharged/transferred to ICF':0,
      'Discharged/transferred to another type of inpatient care institution':0,
      'Discharged/transferred to home with home health service':0,
      'Left AMA':0,
      'Discharged/transferred to home under care of Home IV provider':0,
      'Admitted as an inpatient to this hospital':0,     
      }
      adss = { 'Transfer from Critical Access Hospital' : 0,'Normal Delivery ':0,
      'Sick Baby':0,'Extramural Birth':0,'NULL':0,'Clinic Referral':0,'Not Mapped':0,
      'Transfer from hospital inpt/same fac reslt in a sep claim':0,
      'Transfer from Ambulatory Surgery Center':0,'HMO Referral':0,
      'Transfer from a hospital':0,
      'Transfer from a Skilled Nursing Facility (SNF)':0,
      'Transfer from another health care facility':0,'Emergency Room':0,
      'Court/Law Enforcement':0,
      'Not Available':0}
      aggrr = 0
      if agr == '[0-10)':
         aggrr=5
      elif agr == '[10-20)':
         aggrr = 15
      elif agr == '[20-30)':
         aggrr = 25
      elif agr == '[30-40)':
         aggrr = 35
      elif agr == '[40-50)':
         aggrr = 45
      elif agr == '[50-60)':
         aggrr = 55
      elif agr == '[60-70)':
         aggrr = 65
      elif agr == '[70-80)':
         aggrr = 75
      elif agr == '[80-90)':
         aggrr = 85
      elif agr == '[90-100)':
         aggrr = 90
      wemm = 0
      if wem == 'Yes':
         wemm = 1
      else:
         wemm = 0
      mess = {'Emergency/Trauma':0,'Family/GeneralPractice':0,'InternalMedicine':0,'Nephrology':0,'Orthopedics':0,'Orthopedics-Reconstructive':0,'Other':0,'Radiologist':0,'Surgery-General':0,'UNK':0}

      mess[mes]=adss[ads]=payer[pay]=mett[met]=repp[rep]=natt[nat]=chll[chl]=glimm[glim]=glipp[glip]=glypp[glyb]=pioo[pio]=ross[ros]=acaa[aca]=mmgg[mmg]=troo[tro]=inss[ins]=glyy[gly]=1
      

      scalerfile = 'knn.sav'
      knn_model = pickle.load(open(scalerfile, 'rb'))
      race[rac] = 1
      # res = knn_model.predict([int(hours),int(prolab
      # ,int(prod),int(medic),int(outpat),int(emerg),
      # int(inpat),int(diag)]+list(race.values()))]
      abc = [int(hours),int(prolab),int(prod),int(medic),int(outpat),int(emerg),int(inpat),int(diag)]
      abc1=list(race.values())+list(gender.values())+list(glue.values())+list(aa1c.values())+list(mett.values())+list(repp.values())+list(natt.values())+list(chll.values())+list(glimm.values())+acee+list(glipp.values())+list(glypp.values())+toll+list(pioo.values())+list(ross.values())+list(acaa.values())+list(mmgg.values())+tol+list(troo.values())+list(inss.values())+list(glyy.values())+glipz+glii+megg+merr+comm+[0]+list(payer.values())+list(adtt.values())+list(disc.values())+list(adss.values())+list(mess.values())
      abc=abc+abc1
      abc3=[]
      for i in range(0,144-(len(abc))-3):
         abc3.append(0) 
      abc2 = [int(aggrr)]+[int(wemm)]
      if len(abc) > 142:
         abc=abc+abc2
         print(len(abc))
      else:
         abc=abc+abc3+abc2
         print(len(abc))
      # abc2=abc.reshape(-1, 1)
      print(abc)
      print("Done Modeling")

      # abc=abc[:len(abc)-1]
      arr = np.array(abc)
      arr = arr.reshape(1, -1)
      result = knn_model.predict(arr)
      print("This is the result = ",result)
      return jsonify(str(result[0]))
    else:
      return jsonify('Please Submit to show info')


	# response_object = {'status': 'success'}
	# if request.method == 'POST':
    # 		print("GOT IT")
	# 		# return jsonify('Got the result')
	# else:
	# 		return jsonify('No POST')




@application.route('/Result')#,methods=['POST'])
def get_data():
   return jsonify('Got Results')


if __name__ == '__main__':
    application.run()