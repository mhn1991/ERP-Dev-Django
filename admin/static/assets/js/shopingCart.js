function addToCart(name,code,price,image,tiles,box,pallet){
    var cookies = document.cookie.split(";");
    // we don't have cookie yet 
    if(decodeURIComponent(cookies[0].split("=")[1]) == "undefined" && price != 0){
	//console.log(code); 
	var json= {"items" :[{"name": name,"code":code,"price":price,"image":image,"tiles":tiles,"box":box,"pallet":pallet}]};
	json = JSON.stringify(json);
	setCookie(json);
	makeItem(name,image,code,tiles,box,pallet);
	setTrolley(1);
	setTotal(price);
    }else if (decodeURIComponent(cookies[0].split("=")[1]) != "undefined"){
	var json = JSON.parse(decodeURIComponent(cookies[0].split("=")[1]).split(";")[0]);
	items = json['items'];
	//console.log(items);
	setTrolley(items.length);
	total = 0;
	for(var i = 0 ; i < items.length;i++){
	    if (document.getElementById(items[i]['code']) == null){
		//console.log(items[i]['name']);
		makeItem(items[i]['name'],items[i]['image'],items[i]['code'],items[i]['tiles'],items[i]['box'],items[i]['pallet']);
		total+= items[i]['price'];
	    } 
	    if(items[i]['code'] == code && (items[i]['tiles'] != tiles || items[i]['box'] != box || items[i]['pallet'] != pallet) && price != 0){
		for(var j=0;j<items.length;j++){
		    total+= items[j]['price'];
		}
		total -= items[i]['price'];
		items[i]['tiles'] = tiles;
		items[i]['box'] = box;
		items[i]['pallet'] = pallet;
		items[i]['price'] = price;
		total+= items[i]['price'];
		setCookie(JSON.stringify(json));
		console.log(json);
		updateQuantity(code,tiles,box,pallet);
		setTotal(total);
		break;
	    }
	}
	//setTotal(total);
    }
}



function makeItem(name,image,code,tiles,box,pallet){
    var card = document.getElementById("miniCard");
    var cardItem = document.createElement("div");
    cardItem.setAttribute("class","cart_item");
    //cardItem.setAttribute("id",code);
    var itemPic = document.createElement("div");
    itemPic.setAttribute("class","cart_img");
    var aTag = document.createElement("a");
    aTag.href = "#";
    var imgTag = document.createElement("img");
    imgTag.src= image;
    imgTag.height= 90;
    imgTag.width=90;
    var itemInfo = document.createElement("div");
    itemInfo.setAttribute("class","cart_info");
    var itemName = document.createElement("a");
    var itemQuantity = document.createElement("span");
    itemQuantity.setAttribute("class","quantity");
    itemQuantity.setAttribute("id",code);
    itemQuantity.innerText = "Tiles: "+tiles+" Box: "+box+" Pallet: "+pallet;
    itemName.href = "#";
    itemName.innerHTML = name;
    itemInfo.appendChild(itemName);
    itemInfo.appendChild(itemQuantity);
    aTag.appendChild(imgTag);
    itemPic.appendChild(aTag);
    cardItem.appendChild(itemPic);
    cardItem.appendChild(itemInfo);
    card.appendChild(cardItem);
}

function updateQuantity(code,tiles,box,pallet){
    var item = document.getElementById(code);
    item.innerText = "Tiles: "+tiles+" Box: "+box+" Pallet: "+pallet;
}

function setCookie(json){
    var expirationDate = new Date();                                                                                                                                                                            
    //expires in 10 years
    expirationDate.setTime(expirationDate.getTime() + 3650 * 24* 60 * 60 * 1000);
    var expires = "; expires=" + expirationDate.toUTCString();
    //expires in 10 years
    var maxAge = "; max-age=" + 3650*24*60*60;
    //var cookie = JSON.stringify({"name": name,"code":code,"price":price,"image":image,"tiles":tiles,"box":box,"pallet":pallet});
    cookie = json + expires + maxAge; 
    $.cookie("basket",cookie);
}

function setTrolley(num){
    var Trolley = document.getElementById("trolley");
    Trolley.innerText = num;
}

function setTotal(price){
    var total = document.getElementById("total");
    total.innerText = price;
}

$(document).ready(function(){
    var priceBox = document.getElementById("priceBox");
    priceBox.innerText = 0;
    var boxInput = document.getElementById("boxes");
    boxInput.value = 0;
    var palletInput = document.getElementById("pallet");
    palletInput.value = 0;
    var tilesInput = document.getElementById("tiles");
    tilesInput.value = 0;
});

var cookies = document.cookie.split(";");
if(decodeURIComponent(cookies[0].split("=")[1]) != "undefined"){
    //var json = JSON.parse(decodeURIComponent(cookies[0].split("=")[1]).split(";")[0]);
    $(document).ready(function(){
	addToCart("","","","","","","");
    });
}else{
    setTotal(0);
}
