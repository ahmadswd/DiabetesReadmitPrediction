<template>

<div>
  
  <b-navbar type="dark" variant="faded" style=" background-color: #102332;">
    <b-navbar-nav>
          <a class="navbar-brand" href="#">
          <img src="https://cdn2.iconfinder.com/data/icons/jetflat-buildings/90/008_010_hospital_clinic_building-512.png" style="height:50px; width:50px;" alt="">
        </a>
            <button class="navbar-toggler" style="background-color:#102332" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav ml-auto">

        <li class="nav-item active">
          <a class="nav-link" href="#">General Information</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Input Data</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Show Result</a>
        </li>
      </ul>
    </div>
        </b-navbar-nav>
</b-navbar>
<!--Carousel Wrapper-->
<div id="video-carousel-example" class="carousel slide carousel-fade" data-ride="carousel" >
  <!--Indicators-->
  <ol class="carousel-indicators">
    <li data-target="#video-carousel-example" data-slide-to="0" class="active"></li>
    <li data-target="#video-carousel-example" data-slide-to="1"></li>
    <li data-target="#video-carousel-example" data-slide-to="2"></li>
  </ol>
  <!--/.Indicators-->
  <!--Slides-->
  <div class="carousel-inner" role="listbox">
    <div class="carousel-item active" style='height:400px'>
      <video class="video-fluid" autoplay loop muted >
        <source src="https://mdbootstrap.com/img/video/Tropical.mp4" type="video/mp4" />
      </video>
    </div>
    <div class="carousel-item">
      <video class="video-fluid" autoplay loop muted>
        <source src="https://mdbootstrap.com/img/video/forest.mp4" type="video/mp4" />
      </video>
    </div>
    <div class="carousel-item">
      <video class="video-fluid" autoplay loop muted>
        <source src="https://mdbootstrap.com/img/video/Agua-natural.mp4" type="video/mp4" />
      </video>
    </div>
  </div>
  <!--/.Slides-->
  <!--Controls-->
  <a class="carousel-control-prev" href="#video-carousel-example" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#video-carousel-example" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
  <!--/.Controls-->
</div>
<!--Carousel Wrapper-->
    <router-view/>

  </div>

</template>


<style>
#app {
  margin-top: 60px
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
