document.addEventListener("DOMContentLoaded",function()
{const nameSearch=document.getElementById("name-search")
const tags=document.querySelectorAll(".tag")
const projects=document.querySelectorAll(".project")
function filterProjects()
{const nameQuery=nameSearch.value.toLowerCase();projects.forEach((project)=>{const name=project.getAttribute('data-name')
const nameMatch=name.includes(nameQuery)
if(nameMatch)
{project.style.display="";}else
{project.style.display="none";}})}
tags.forEach((tag)=>{tag.addEventListener("click",function()
{const selectedTag=this.getAttribute("data-tag")
projects.forEach((project)=>{const projectTags=project.getAttribute("data-tags")
if(projectTags.includes(selectedTag))
{project.style.display=""}else
{project.style.display="none"}})})})
nameSearch.addEventListener("keyup",filterProjects)});let slideIndex=1;showSlides(slideIndex)
function moveSlide(n)
{slideIndex+=n
showSlides(slideIndex)}
function showSlides(n)
{let slides=document.getElementsByClassName("carousel-item")
if(n>slides.length)
{slideIndex=1}
if(n<1)
{slideIndex=slides.length;}
for(let i=0;i<slides.length;i++)
{slides[i].style.display="none"}
slides[slideIndex-1].style.display="flex"};