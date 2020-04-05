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
                  <h1 class="pt-2">Guidelines</h1>
                    <div class="px-4">
                        <div class="row justify-content-center">
                            <!-- content -->
                                    <div class="col-lg-9">
                                        <div style="text-align: left">
                                            <p>Congratulations, you are on your way to being an expert fake
                                                news spotter. For more tips and tricks, click on any of the SAMS
                                                icons below. You will find a complete list of warning signs that
                                                might suggest you have fake news in your hands.</p>
                                        </div>
                                        <!-- Tabs with icons -->
                                        <tabs fill class="flex-column flex-md-row">
                                            <card shadow slot-scope="{}">
                                                <tab-pane key="tab1">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="search-location" />
                                                        <i class="ni mr-2"/>
                                                        Source
                                                    </template>
                                                    <div style="text-align: left">
                                                        <p> Taking a critical look at the source, both in and of the news, is the first step.</p>
                                                        <p> What to check for :</p>
                                                    </div>
                                                    <ul class="list" style="text-align: left">
                                                        <li>Where did the information originate (e.g. WHO World Health Organization)
                                                            <ul class="list" style="text-align: left">
                                                                <li>A reverse search confirms the source</li>
                                                                <li>The web address is correct</li>
                                                                <li>The "About us" section of the source media confirms reliability</li>
                                                            </ul>
                                                        </li>
                                                        <li>Sources referred to (a group of researchers vs. a named individual or institution)
                                                            <ul class="list" style="text-align: left">
                                                                <li>In-text references and quotes can be sourced</li>
                                                                <li>Avoid anonymous sources</li>
                                                            </ul>
                                                        </li>
                                                        <li>How you got access to the information (on Facebook)</li>
                                                    </ul>
                                                </tab-pane>

                                                <tab-pane key="tab2">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="user-edit" />
                                                        <i class="ni mr-2"/>
                                                        Authors
                                                    </template>
                                                    <div style="text-align: left">
                                                        <p>The author is a trusted source. It could be a journalist, an editorial office or a news agency.</p>
                                                        <p>What to check for :</p>
                                                    </div>
                                                    <ul class="list" style="text-align: left">
                                                        <li>Author names mentioned</li>
                                                        <li>Other references to the same author to confirm credibility</li>
                                                        <li>Author's professional affiliations, academic or professional credentials</li>
                                                        <li>Other or related publications by the same author</li>
                                                    </ul>
                                                </tab-pane>

                                                <tab-pane key="tab3">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="file-alt" />
                                                        <i class="ni mr-2"/>
                                                        Message
                                                    </template>
                                                    <div style="text-align: left">
                                                        <p>The message should be clear, balanced and unbiased.</p>
                                                        <p>What to check for :</p>
                                                    </div>
                                                    <ul class="list" style="text-align: left">
                                                        <li>Unsupported or outrageous claims</li>
                                                        <li>A push to share the information</li>
                                                        <li>A lack of quotes, references or contributing sources</li>
                                                        <li>Headlines that provoke strong emotions</li>
                                                        <li>Ease of cross-checking in multiple & reputable sources</li>
                                                    </ul>
                                                </tab-pane>
                                                <tab-pane key="tab4">
                                                    <template slot="title">
                                                        <font-awesome-icon icon="spell-check" />
                                                        <i class="ni mr-2"/>
                                                        Spelling
                                                    </template>
                                                    <div style="text-align: left">
                                                        <p>Reputable sources will proofread material prior to publishing.</p>
                                                        <p>What to check for :</p>
                                                    </div>
                                                    <ul class="list" style="text-align: left">
                                                        <li>Repeated spelling mistakes</li>
                                                        <li>Poor grammar</li>
                                                        <li>Incorrect punctuation</li>
                                                        <li>Use of different fonts</li>
                                                        <li>Entire words/phrases written in CAPITAL LETTERS</li>
                                                    </ul>
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
