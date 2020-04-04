<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                <img src="img/brand/white.png" alt="logo">
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/">
                        <img src="img/brand/blue.png">
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
                <div class="nav-item" menu-classes="dropdown-menu-xl">
                  <router-link slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button" to="/">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span class="nav-link-inner--text">Vs Faker</span>
                  </router-link>
                </div>
                <div tag="li" class="nav-item">
                  <router-link slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button" to="/guidelines">
                        <i class="ni ni-collection d-lg-none"></i>
                        <span class="nav-link-inner--text">General Guidelines</span>
                  </router-link>
                </div>
            </ul>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
//import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    //BaseDropdown
  }
};
</script>
<style>
</style>
