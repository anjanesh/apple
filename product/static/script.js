let trs;
document.addEventListener("DOMContentLoaded", () =>
{
    let tbl_products = document.getElementById('tbl-products');
    if (tbl_products)
    {
        let tbl_products_tbody_trs = tbl_products.querySelectorAll('tbody > tr');
        trs = [...tbl_products_tbody_trs];    
    }

});      

document.addEventListener("DOMContentLoaded", () =>
{
    if (document.getElementById('search'))
    {
        document.getElementById('search').addEventListener('input', (e) =>
        {
            let search = e.target.value;
            
            trs.forEach(tr =>
            {
                let found = false;
    
                [...tr.children].forEach(child =>
                {
                    if (child.localName == 'th') return;
                    let cell = child.innerHTML.trim();                    
    
                    if (cell.toLowerCase().includes(search.toLowerCase()))
                    {
                        found = true;
                        return;
                    }
                });
                
                tr.style.display = found ? 'table-row' : 'none';
                
            });
        });    
    }
});