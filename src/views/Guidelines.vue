<template>
    <div class="guidelines-page">
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section class="section section-skew">
            <div class="container">
                <card shadow class="card-profile mt--300" no-body>
                  <h1>ifuhsdafoiuhwouefw eFOIUWehiofuaz </h1>
                  <p>fdsuhiufh sdvusdhfhasiu iodsuhfiousad isudhiushad oiuhf
                   disuhfiusah fisudhfiushd oiushfiousdhafoiu </p>
                    <div class="px-4">
                        <div class="row justify-content-center">
                            <!-- content -->
                                    <div class="col-lg-9">
                                        <!-- Tabs with icons -->
                                        <tabs fill class="flex-column flex-md-row">
                                            <card shadow slot-scope="{}">
                                                <tab-pane key="tab1">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="search-location" />
                                                        <i class="ni mr-2"/>
                                                        Source
                                                    </template>
                                                    <p class="description">Source Source Source Source Source Source Source Source
                                                        Source Source Source Source Source Source Source Source Source Source
                                                        Source Source Source Source Source Source Source Source Source Source </p>
                                                </tab-pane>

                                                <tab-pane key="tab2">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="user-edit" />
                                                        <i class="ni mr-2"/>
                                                        Authors
                                                    </template>
                                                    <p class="description">Authors Authors Authors Authors Authors Authors Authors Authors
                                                        Authors Authors Authors Authors Authors Authors Authors Authors Authors Authors
                                                        Authors Authors Authors Authors Authors Authors Authors Authors Authors Authors </p>
                                                </tab-pane>

                                                <tab-pane key="tab3">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="file-alt" />
                                                        <i class="ni mr-2"/>
                                                        Message
                                                    </template>
                                                    <p class="description">Message Message Message Message Message Message
                                                        Message Message Message Message Message Message Message Message Message Message
                                                        Message Message Message Message Message Message Message Message </p>
                                                </tab-pane>
                                                <tab-pane key="tab4">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="spell-check" />
                                                        <i class="ni mr-2"/>
                                                        Spelling
                                                    </template>
                                                    <p class="description">Spelling Spelling Spelling Spelling
                                                        Spelling Spelling Spelling Spelling Spelling Spelling
                                                        Spelling Spelling Spelling Spelling Spelling Spelling </p>
                                                </tab-pane>
                                            </card>
                                        </tabs>
                                    </div>
                            <!-- end of content -->
                        </div>
                    </div>
                </card>
            </div>
        </section>
    </div>
</template>
<script>
    import Tabs from "@/components/Tabs/Tabs.vue";
    import TabPane from "@/components/Tabs/TabPane.vue";
    export default {
        components: {
            Tabs,
            TabPane
        }
    };
</script>
<style>
</style>
