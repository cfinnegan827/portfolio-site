window.onload = function(){
    //get executed onces everything is done loading
    r = new X.renderer3D();
    r.init()

    //create a new cube and change its color using rgb from 0 to 1
    c = new X.cube();
    c.color = [1,0,0];

    r.add(c);

    r.render();

    r.interactor.onMouseWheel = function(event) {
    // prevent zoom on scroll
    event.preventDefault();
    return false;
    };
}
