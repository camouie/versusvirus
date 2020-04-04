<template>
  <div>
  <svg >
    <defs>
      <marker id="m-end" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth" >
        <path d="M0,0 L0,6 L9,3 z"></path>
      </marker>
    </defs>
  </svg>
    <d3-network ref='net' :net-nodes="nodes" :net-links="links" :options="options"  :link-cb="lcb"/>
</div>
</template>

<script>
import D3Network from 'vue-d3-network';
export default {
  name: "graph_test",
  components: {
    D3Network
  },
  data () {
    return {
      nodes: [
        { id: 1, name: 'my awesome node 1'},
        { id: 2, name: 'my node 2'},
        { id: 3, name:'orange node', _color: 'orange' },
        { id: 4, name:'blue node',_color: '#00aaff'},
        { id: 5 },
        { id: 6 },
        { id: 7 },
        { id: 8 },
        { id: 9 },
        { id: 10 },
        { id: 11 },
        { id: 12 },
        { id: 13 },
        { id: 14 },
      ],
      links: [
        { sid: 1, tid: 2 },
        { sid: 2, tid: 8 },
        { sid: 4, tid: 3 },
        { sid: 4, tid: 5 },
        { sid: 4, tid: 9 },
        { sid: 5, tid: 6 },
        { sid: 7, tid: 8 },
        { sid: 5, tid: 8 },
        { sid: 3, tid: 8 },
        { sid: 7, tid: 9 },
        { sid: 3, tid: 9 },
        { sid: 10, tid: 6 },
        { sid: 11, tid: 6 },
        { sid: 12, tid: 6 },
        { sid: 13, tid: 6 },
        { sid: 14, tid: 6 }

      ],
      nodeSize:10,
      canvas:false

    }
  },
  computed:{
    options(){
      return{
        force: 3000,
        size:{ w:600, h:600},
        nodeSize: this.nodeSize,
        nodeLabels: true,
        canvas: this.canvas,
        linkWidth:2
      }
    }
  },
  methods:{
    lcb (link) {
      link._svgAttrs = { 'marker-end': 'url(#m-end)'}
      return link
    }
  }
};
</script>

<style src="vue-d3-network/dist/vue-d3-network.css">
path{
  fill: rgba(18, 120, 98, 0.8) !important;
}
</style>
