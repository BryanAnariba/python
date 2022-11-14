const API='http://127.0.0.1:8000/api/companies/'
window.onload = () => {
    fetch( `${ API }` )
    .then( res => res.json() )
    .then( res => console.log( res ) );
}