
<style scope>
.chip.chip-md {
height: 42px;
line-height: 42px;
border-radius: 21px;
}
.chip.chip-md img {
height: 42px;
width: 42px;
}

.chip.chip-lg {
height: 52px;
line-height: 52px;
border-radius: 26px;
}
.chip.chip-lg img {
height: 52px;
width: 52px;
}
</style>

<template>
<div id="app">
<div class="container">
</div>
<div>
<b-form @submit="onSubmit" class="w-100">
<b-container> <!--class="bv-example-row"> -->
<!-- <b-row> -->
<!-- This is the left nav bar -->

<!-- <img src="https://visualpharm.com/assets/351/Male%20User-595b40b85ba036ed117da579.svg" -->
<!-- id ="ico" style="height:100%; width:100%; position: absolute;top:0 bottom:0" alt=""> -->
<!-- </b-row> -->
<vue-snotify></vue-snotify>

<div class="chip chip-lg" >
  <img src="../assets/as.jpg" alt="Contact Person"> Ahmad Sweed
</div>

<b-row>
<b-col sm="12">
<br>
<br>
<p>Please fill the infromation below....</p>
</b-col>
<!-- This is the actual contect -->
</b-row>
<b-row>
<b-col sm="1"></b-col>

<b-col sm="10">
<b-button v-b-toggle.collapse-1 style="background-color:#102332" variant="primary">Add Infomration</b-button>
<b-collapse id="collapse-1" class="mt-2">
<b-card style="text-align=center">
<p class="card-text">Please enter the patient information below...</p>
<!-- <b-button v-b-toggle.collapse-1-inner size="sm">Toggle Inner Collapse</b-button> -->
<div class="form-group">
<b-container>
<b-row>
<b-col>
      <!-- <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-b-form-input"> -->
          <!-- <b-form-b-form-input id="form-title-b-form-input"
                        type="text"
                        v-model="InfoGetting.title"
                        required
                        placeholder="Enter title">
          </b-form-b-form-input> -->
        <!-- </b-form-group>   -->
<label for="exampleFormControlSelect1"><strong>General Info</strong></label>
<b-form-input type="number" v-model="InfoGetting.hrs" id="hrs"  class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Hours"></b-form-input> 
<small id="helpId" class="form-text text-muted"></small>
<b-form-input type="number" v-model="InfoGetting.lab" id="lab" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Lab Procedures"></b-form-input>
<small id="helpId" class="form-text text-muted"></small>
<b-form-input type="number" v-model="InfoGetting.pro" id="pro" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Procedures"></b-form-input>
<small id="helpId" class="form-text text-muted"></small>
</b-col>

</b-row>
  </br>
  <label for="exampleFormControlSelect1"><strong>Health Info</strong></label>


<b-row>
  <b-col sm="6">
  <b-form-input type="number" v-model="InfoGetting.med" id="med" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Medications"></b-form-input>
  <small id="helpId" class="form-text text-muted"></small>
  <b-form-input type="number" v-model="InfoGetting.out" id="out" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Outpatient"></b-form-input>
  </b-col>    
  <b-col sm="6">    
  <small id="helpId" class="form-text text-muted"></small>
  <b-form-input type="number" v-model="InfoGetting.eme" id="eme" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Emergency"></b-form-input>
  <small id="helpId" class="form-text text-muted"></small>
  <b-form-input type="number" v-model="InfoGetting.inp" id="inp" class="form-control" value="" min="0" max="1000" step="1" placeholder="# of Inpatient"></b-form-input>
  </b-col>
</b-row>

</br>

<b-row>

  <b-col sm="12">
  <small id="helpId" class="form-text text-muted"></small>
  <b-form-input type="number" v-model="InfoGetting.dig" id="dig" class="form-control" value="" min="0" step="1" placeholder="# of Diagnoses"></b-form-input>
  </b-col>   
</b-row>
</br>
<b-row>
<b-col sm="12">
  <label for="exampleFormControlSelect1">Admission Type</label>
<div class="form-group">
  <select v-model="InfoGetting.adt" class="form-control" id="adt">
  <option>Urgent</option>
  <option>Elective</option>
  <option>Newborn</option>
  <option>Not Available</option>
  <option>Null</option>
  <option>Trauma Center</option>
  <option>Not Mapped</option>
  </select>
  </div>
</b-col>
</b-row>
<b-row>
<b-col sm="12">
  <label for="exampleFormControlSelect1">Admission Source</label>
<div class="form-group">
  <select v-model="InfoGetting.ads" class="form-control" id="ads">
  <option>Clinic Referral</option>
  <option>HMO Referral</option>
    <option>Transfer from a hospital</option>
  <option>Transfer from a Skilled Nursing Facility(SNF)</option>
  <option>Transfer from Another Health Care Facility</option>
  <option>Emergency Room</option>
  <option>Court/Law Enforcement</option>
  <option>Not Available</option>
  <option>Transfer from Critical Access Hospital</option>
  <option>Normal Delivery</option>
  <option>Sick Baby</option>
  <option>Null</option>
  <option>Not Mapped</option>
  <option>Transfer from Hospital Inpt/Same fac Reslt in a Sep Claim</option>
  <option>Transfer from Ambulatory Surgery Center</option>

  </select>
  </div>
</b-col>
</b-row>
<b-row>
<b-col sm="12">
  <label for="exampleFormControlSelect1">Discharge Disposition</label>
<div class="form-group">
  <select v-model="InfoGetting.did" class="form-control" id="did">
  <option>Discharged/transferred to another short term hospital</option>
  <option>Discharged/transferred to SNF</option>
  <option>Discharged/transferred to ICF</option>
  <option>Discharged/transferred to another type of inpatient care</option>
  <option>Discharged/transferred to home with home health service</option>
  <option>Left AMA</option>
  <option>Discharged/transferred to home under care of Home IV</option>
  <option>Admitted as an inpatient to this hospital</option>
  <option>Neonate discharged to another hospital for neonatal</option>
  <option>Still patient or expected to return for outpatient services</option>
  <option>Still patient or expected to return for outpatient services</option>
  <option>Discharged/transferred/referred another institution for outpatient services</option>
  <option>Discharged/transferred/referred to this institution for outpatient services</option>
  <option>Discharged/transferred to another rehab fac including rehab units of a hospital</option>
  <option>Discharged/transferred to a long term care hospital</option>
  <option>Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare</option>
  <option>Not Mapped</option>
  <option>Discharged/transferred to a federal health care facility</option>
  <option>Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital</option>
  </select>
  </div>
</b-col>
</b-row>

<b-row>
<b-col sm="12">
  <label for="exampleFormControlSelect1">Medical Speciality</label>
<div class="form-group">
  <select v-model="InfoGetting.mes" class="form-control" id="mes">
  <option>Emergency/Trauma</option>
  <option>Family/GeneralPractice</option>
  <option>InternalMedicine</option>
  <option>Nephrology</option>
  <option>Orthopedics</option>
  <option>Orthopedics-Reconstructive</option>
  <option>Other</option>
  <option>Radiologist</option>
  <option>Surgery-General</option>
  <option>UNK</option>

  </select>
  </div>
</b-col>
</b-row>


<b-row>
  <b-col sm="12">
  <label for="exampleFormControlSelect1">Payer</label>
  <div class="form-group">
  <select v-model="InfoGetting.pay" class="form-control" id="pay">
  <option>FR</option>
  <option>MP</option>
  <option>OG</option>
  <option>OT</option>
    <option>WC</option>
  <option>PO</option>
    <option>CH</option>
  <option>CM</option>
    <option>DM</option>
  <option>SI</option>
    <option>CP</option>
  <option>SP</option>
    <option>BC</option>
  <option>UN</option>
    <option>HM</option>
  <option>MD</option>
    <option>MC</option>
  <option>UNK</option>
  </select>
  </div>
  </b-col>
</b-row>
</br>
  <label for="exampleFormControlSelect1"><strong>Personal Info</strong></label>
<b-row>
  <b-col sm="8">
  <div class="form-group">
  <label for="exampleFormControlSelect1">Race</label>
  <select v-model="InfoGetting.rac" class="form-control" id="rac">
  <option>Asian</option>
  <option>Caucasian</option>
  <option>Hispanic</option>
  <option>Other</option>
  <option>UNK</option>
  </select>
  </div>
  </b-col>
  <b-col sm="4">
  <div class="form-group">
  <label for="exampleFormControlSelect1">Gender</label>
  <select v-model="InfoGetting.gen" class="form-control" id="gen">
  <option>Male</option>
  <option>Female</option>
  <option>Other</option>
  </select>
  </div>
  </b-col>
</b-row>

<b-row>

  <b-col sm="8">
  <div class="form-group">
  <label for="exampleFormControlSelect1">Age Range</label>
  <select v-model="InfoGetting.agr" class="form-control" id="agr">
  <option>[0-10)</option>
  <option>[10-20)</option>
  <option>[20-30)</option>
  <option>[30-40)</option>
  <option>[40-50)</option>
  <option>[50-60)</option>
  <option>[60-70)</option>
  <option>[70-80)</option>
  <option>[80-90)</option>
  <option>[90-100)</option>
  </select>
  </div>
  </b-col>
  <b-col sm="4">
<div class="form-group">
  <label for="exampleFormControlSelect1">Weight Measured?</label>
  <select v-model="InfoGetting.wem" class="form-control" id="wem">
  <option>Yes</option>
  <option>No</option>
  </select>
  </div>
  </b-col>
</b-row> 
 


</br>
    <label for="exampleFormControlSelect1"><strong>Test Results</strong></label>

<b-row>
  <b-col sm="6">
  <label for="exampleFormControlSelect1">Glucose Serum Test</label>
  <div class="form-group">
  <select v-model="InfoGetting.gls" class="form-control" id="gls">
  <option> > 300</option>
  <option>Norm</option>
  <option>None</option>
  </select>
  </div>
  </b-col>
  <b-col sm="6">
  <label for="exampleFormControlSelect1">A1c Test</label>
  <div class="form-group">
  <select v-model="InfoGetting.a1c" class="form-control" id="a1c">
  <option> > 8</option>
  <option>Norm</option>
  <option>None</option>
  </select>
  </div>
  </b-col>
</b-row>
  <span class="border-0">
<b-row>
  <b-col sm="12">
  <label for="exampleFormControlSelect1">Change of Meds</label>
  <div class="form-group">
  <select v-model="InfoGetting.com" class="form-control" id="com">
  <option>Yes</option>
  <option>No</option>
  </select>
  </div>
  </b-col>
  
</b-row>
</span>

<b-row>
  <b-col sm="3">
  <label for="exampleFormControlSelect1">Metformin</label>
  <div class="form-group">
  <select v-model="InfoGetting.met" class="form-control" id="met">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Repaglinide</label>
  <div class="form-group">
  <select v-model="InfoGetting.rep" class="form-control" id="rep">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Nateglinide</label>
  <div class="form-group">
  <select v-model="InfoGetting.nat" class="form-control" id="nat">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Chlorpropamide</label>
  <div class="form-group">
  <select v-model="InfoGetting.chl" class="form-control" id="chl">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>
</b-row>

<b-row>
  <b-col sm="3">
  <label for="exampleFormControlSelect1">Glimepiride</label>
  <div class="form-group">
  <select v-model="InfoGetting.glim" class="form-control" id="glim">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Acetohexamide</label>
  <div class="form-group">
  <select v-model="InfoGetting.ace" class="form-control" id="ace">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Glipizide</label>
  <div class="form-group">
  <select v-model="InfoGetting.glip" class="form-control" id="glip">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Glyburide</label>
  <div class="form-group">
  <select v-model="InfoGetting.glyb" class="form-control" id="glyb">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>
</b-row>

<b-row>
  <b-col sm="3">
  <label for="exampleFormControlSelect1">Tolbutamide</label>
  <div class="form-group">
  <select v-model="InfoGetting.tol" class="form-control" id="tol">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Pioglitazone</label>
  <div class="form-group">
  <select v-model="InfoGetting.pio" class="form-control" id="pio">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Rosiglitazone</label>
  <div class="form-group">
  <select v-model="InfoGetting.ros" class="form-control" id="ros">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Acarbose</label>
  <div class="form-group">
  <select v-model="InfoGetting.aca" class="form-control" id="aca">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>
</b-row>

<b-row>
  <b-col sm="3">
  <label for="exampleFormControlSelect1">mMglitol</label>
  <div class="form-group">
  <select v-model="InfoGetting.mmg" class="form-control" id="mmg">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Tolazamide</label>
  <div class="form-group">
  <select v-model="InfoGetting.tro" class="form-control" id="tro">
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Insulin</label>
  <div class="form-group">
  <select v-model="InfoGetting.ins" class="form-control" id="ins">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="3">
  <label for="exampleFormControlSelect1">Glyburide Metformin</label>
  <div class="form-group">
  <select v-model="InfoGetting.gly" class="form-control" id="gly">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>
</b-row>

<b-row>
  <b-col sm="4">
  <label for="exampleFormControlSelect1">Glipizide-Metformin</label>
  <div class="form-group">
  <select v-model="InfoGetting.gli" class="form-control" id="gli">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="4">
  <label for="exampleFormControlSelect1">Glimepiride-Pioglitazone</label>
  <div class="form-group">
  <select v-model="InfoGetting.glp" class="form-control" id="glp">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>

  <b-col sm="4">
  <label for="exampleFormControlSelect1">Metformin-Rosiglitazone</label>
  <div class="form-group">
  <select v-model="InfoGetting.mer" class="form-control" id="mer">
  <option>No</option>
  <option>Steady</option>
  <option>Up</option>
  </select>
  </div>
  </b-col>
</b-row>


</b-container>
</div>
<button type="submit" style="background-color:#102332;" class="btn btn-primary">Submit</button>
<b-collapse id="collapse-1-inner" class="mt-2">
</b-collapse>
</b-card>
</b-collapse>


</b-col>
<b-col sm="2"></b-col>
</b-row>

</b-container>
</b-form>
<b-row>
<b-col sm="12">
</br>
</br>
<div style="text-align:center">
<h1>{{ msg }}</h1>
</div>
</b-col>
</b-row>
</div>
</div>

</template>

<script>
import axios from 'axios';
import Vue from 'vue';
import Snotify from 'vue-snotify';
import 'vue-snotify/styles/material.css';
Vue.use(Snotify);

export default {
name: 'Ping',
data() {
return {
msg: 'Getting Result...',
      InfoGetting: {
        hrs: '',
        lab: '',
        pro: '',
        med: '',
        out: '',
        eme: '',
        inp: '',
        dig: '',
        adt: '',
        ads: '',
        did: '',
        mes: '',
        pay: '',
        rac: '',
        gen: '',
        agr: '',
        wem: '',
        gls: '',
        a1c: '',
        com: '',
        met: '',
        rep: '',
        nat: '',
        chl: '',
        glim: '',
        ace: '',
        glip: '',
        glyb: '',
        tol: '',
        pio: '',
        ros: '',
        aca: '',
        mmg: '',
        tro: '',
        ins: '',
        gly: '',
        gli: '',
        glp: '',
        mer: '',   
        title: '',
        author: '',
        read: [],
      },
};
},
methods: {
displayNotification() {
  // var utc = new Date().toJSON().slice(0,10).replace(/-/g,'/');

this.$snotify.error('Patient 68% possible to readmittion within the next 30 days')//'Patient will readmit within the next 30 days between ' + str(utc) + ' and ' + str(utc+30));
},
displayNotificationNo(){
  this.$snotify.success('Patient 68% to not readmit  within the next 30 days ')
},
getMessage() {
const path = 'https://sweedcodrp.herokuapp.com';
axios.get(path)
.then((res) => {
this.msg = res.data;
})
.catch((error) => {
// eslint-disable-next-line
this.msg = 'Getting Result...'
console.error(error);
});
},
 onSubmit(evt) {
      evt.preventDefault();
      const path = 'https://sweedcodrp.herokuapp.com';
      const payload = {
    title: this.InfoGetting.title,
    hrs: this.InfoGetting.hrs,
    lab: this.InfoGetting.lab,
    pro: this.InfoGetting.pro,
    med: this.InfoGetting.med,
    out: this.InfoGetting.out,
    eme: this.InfoGetting.eme,
    inp: this.InfoGetting.inp,
    dig: this.InfoGetting.dig,
    adt: this.InfoGetting.adt,
    ads: this.InfoGetting.ads,
    did: this.InfoGetting.did,
    mes: this.InfoGetting.mes,
    pay: this.InfoGetting.pay,
    rac: this.InfoGetting.rac,
    gen: this.InfoGetting.gen,
    agr: this.InfoGetting.agr,
    wem: this.InfoGetting.wem,
    gls: this.InfoGetting.gls,
    a1c: this.InfoGetting.a1c,
    com: this.InfoGetting.com,
    met: this.InfoGetting.met,
    rep: this.InfoGetting.rep,
    nat: this.InfoGetting.nat,
    chl: this.InfoGetting.chl,
    glim: this.InfoGetting.glim,
    ace: this.InfoGetting.ace,
    glip: this.InfoGetting.glip,
    glyb: this.InfoGetting.glyb,
    tol: this.InfoGetting.tol,
    pio: this.InfoGetting.pio,
    ros: this.InfoGetting.ros,
    aca: this.InfoGetting.aca,
    mmg: this.InfoGetting.mmg,
    tro: this.InfoGetting.tro,
    ins: this.InfoGetting.ins,
    gly: this.InfoGetting.gly,
    gli: this.InfoGetting.gli,
    glp: this.InfoGetting.glp,
    mer: this.InfoGetting.mer,
     // property shorthand
  };
      axios.post(path, payload)
        .then(response => {
          // this.getBooks();
          // this.message = 'Book added!';
          // this.makeToast('success', 'b-toaster-bottom-left', true);
          // this.displayNotification();
          // this.showMessage = true;
          console.log('GOT THE MESSAGE')
          alert(response.data)
          if(response.data == "1"){
          this.msg = "This Patient Will readmit"
          this.displayNotification();
          }
          else{
          this.msg = "This Patient Won't readmit"
          this.displayNotificationNo();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log('Got it');
          alert(response)
        });
      // this.$refs.addBookModal.hide();
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      // const payload = {
      //   title: this.addBookForm.title,
      //   author: this.addBookForm.author,
      //   read, // property shorthand
      },
},
created() {
this.getMessage();
},
};
</script>


