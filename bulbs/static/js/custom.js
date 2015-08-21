/* modules for inside thread content */ 

function postOptions() {
    var postOptionTrigger = $(".thread-post"); 
    this.postOptionElement;
    
    $(".post-options").hide();

    postOptionTrigger.mouseenter(function() {
        this.postOptionElement = $(this).children()
            .next()
            .children()
            .closest(".post-options");
            
        this.postOptionElement.show(900);
        //this.postOptionElement.prop("css") += 0.1;
        
        //while (var i = 0; this.postOptionElement.prop("opacity") < 1; i++) {
        //    this.postOptionElement.css("opacity", "+=0.1");
        //}
        
    });
    
    postOptionTrigger.mouseleave(function() {
        //while (var i = 0; this.postOptionElement.prop("opacity") != 0; i++) {
        //    this.postOptionElement.css("opacity", "-=0.1");
       // }
        
        this.postOptionElement.stop(true)
        
        //window.setTimeout(function() {
        this.postOptionElement.hide(900);
        //}, 2000);
        
    });
}


$(function() {
    //postOptions();
    
});
