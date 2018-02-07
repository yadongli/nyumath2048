{%- extends 'slides_reveal.tpl' -%}

{% block input_group -%}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}

{%- block header -%}
{{ super() }}

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<style type="text/css">
//div.output_wrapper {
//  margin-top: 0px;
//}
.input_hidden {
  display: none;
//  margin-top: 5px;
}
</style>

<!-- script>
$(document).ready(function(){
  $(".output_wrapper").click(function(){
      $(this).prev('.input_hidden').slideToggle();
  });
})
</script -->

{%- endblock header -%}

{% block body %}

{{ super() }}


    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: false }
        }
    });
    </script>

<script>

Reveal.initialize({

    // Display controls in the bottom right corner
    controls: false,

    // Display a presentation progress bar
    progress: false,

    // Push each slide change to the browser history
    history: false,

    // Enable keyboard shortcuts for navigation
    keyboard: true,
    slideNumber: true,

    // Enable touch events for navigation
    touch: true,

    // Enable the slide overview mode
    //overview: true,

    // Vertical centering of slides
    //center: true,

    // Loop the presentation
    //loop: false,

    // Change the presentation direction to be RTL
    //rtl: false,

    // Number of milliseconds between automatically proceeding to the
    // next slide, disabled when set to 0, this value can be overwritten
    // by using a data-autoslide attribute on your slides
    //autoSlide: 0,

    // Enable slide navigation via mouse wheel
    mouseWheel: false,

    // Transition style
    // transition: 'concave', // default/cube/page/concave/zoom/linear/fade/none

    // Transition speed
    //transitionSpeed: 'default', // default/fast/slow

    // Transition style for full page backgrounds
    //backgroundTransition: 'default', // default/linear/none

    // Theme
     // width: 100%,
     // height: 100%,
     // margin: 0,
     theme: 'white', // available themes are in /css/theme
});

// remap F5/ESC/b key
Reveal.configure({
  keyboard: {
    66: 'right',
    116: 'left',
    27: 'left'
  }
});

</script>

{% endblock body %}
