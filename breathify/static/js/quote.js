var text = [
    '<i>"Act the way that you want to feel"</i><br /><b>Gretchen Rubin</b></p>',
    '<i>"Tension is who you think you should be. Relaxation is who you are."</i><br /><b>Chinese Proverb</b></p>',
    '<i>"Its not stress that kills us, it is our reaction to it"</i><br /><b>Hans Selye</b></p>',
    '<i>"The time to relax is when you dont have time for it"</i><br /><b> Sydney Harris</b></p>',
    '<i>"Surrender to what is. Let go of what was. Have faith in what will be."</i><br /><b>Sonia Ricotte</b></p>',
    '<i>"Your calm mind is the ultimate weapon against your challenges. So relax"</i><br /><b>Bryant McGill</b></p>',
    '<i>"Feelings come and go like clouds in a windy sky. Conscious breathing is my anchor."</i><br /><b>Thich Nhat Hanh</b></p>',
    '<i>"Trust yourself. You have survived a lot, and you will survive whatever is coming."</i><br /><b>Robert Tew</b></p>',
    '<i>"Your mind will answer most questions if you learn to relax and wait for the answer."</i><br /><b>William Burroughs</b></p>',
    '<i>"TKeep walking through the storm. Your rainbow is waiting on the other side"</i><br /><b>Heather Stillufsen</b></p>',
    '<i>"Surrender to what is. Let go of what was. Have faith in what will be."</i><br /><b>Sonia Ricotte</b></p>'
];
var counter = 0;
var elem = document.getElementById("quote");
var inst = setInterval(change, 8000);

function change() {
    elem.innerHTML = text[counter];
    counter++;
    if (counter >= text.length) {
        counter = 0;
    }
}