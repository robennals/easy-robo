
let walls;
let bricks;
let org;
let player;
let coins;
let score = 0;
//let levelBar1;
let spikes;
let rope;
let bFloor;
let trampo;
let enemy;
let levelPortals;
let isMenuScreen = true;

function setup() {
	new Canvas(800,800)
	world.gravity.y = 10
	
	bricks = new Group();
	bricks.w = 50
	bricks.h = 10
	bricks.color = "brown"
	bricks.collider = "static"
	bricks.tile = "-"
	let floor = new bricks.Sprite();
	floor.y = 600
	floor.w = 1000000000
	floor.x = 400
	floor.h = 3
	
	bFloor = new Group();
	bFloor.w = 50
	bFloor.h = 10
	bFloor.color = "green"
	bFloor.collider = "static"
	bFloor.tile = "b"
	
	trampo = new Group();
	trampo.w = 50
	trampo.h = 15
	trampo.color = "blue"
	trampo.collider = "static"
	trampo.tile = "t"
	
	spikes = new Group();
	spikes.h = 20
	spikes.w = 15
	spikes.color = "red"
	spikes.collider = "static"
	spikes.tile = "z"
	
	rope = new Group();
	rope.h = 150
	rope.w = 5
	rope.color = "yellow"
	rope.collider = "none"
	rope.tile = "l"
	
	enemy = new Group();
	enemy.d = 30
	enemy.color = "green"
	enemy.collider = "dynamic"
	enemy.tile = "e"
	
	walls = new Group();
	walls.w = 10
	walls.h = 150
	walls.color = "black"
	walls.collider = "static"
	walls.tile = "="
	
	coins = new Group();
	coins.diameter = 25
	coins.color = "gold"
	coins.collider = "none"
	coins.tile = "x"
	
	levelPortals = new Group();
	levelPortals.w = 10
	levelPortals.h = 30
	levelPortals.color = "purple"
	
	let levelOne = new levelPortals.Sprite();
	levelOne.x = 100
	levelOne.y = 100
	levelOne.level = 1
	
	let levelTwo = new levelPortals.Sprite();
	levelTwo.x = 200
	levelTwo.y = 200
	levelTwo.level = 2
	
	
	player = new Sprite(400,500)
	player.color = "grey"
	player.collider = "dynamic"
	player.diameter = 30
	player.rotationDrag = 3

// loadLevel();
		
	move(enemy)
}


function loadLevelOne() {
	org = new Tiles([
		//"=b=xxxxb x--=--x-=-=-x-=xxx=---=---=xx   -z=x-z--x--x-=z-x- --x--x-x-l",
		//"=b=bbbbx x--xx--=--=----x----==- e---x=   z z--z-x--z -===-x --lxl----x",
		//"=x=bbb=b   -x--e---x--x-=e-exxx--  = xx    -=--zx-- -xx-xxx- --lxxxxzlx",
		//"=x=xxxx  -=--x--x-x-= -=-xx--=-- = -x   -z== z-x-x---xx-z- x-lxx--x--",
		//"=x=xbbtxl-x--x--=--x--x--=e==--e---x--   x-zz xx--=-x--x- l--x-x-ll=",
		//"=x=bbbxxxtz=e---------------------=---=   zz xxx-=xxzzx-xx-x xxxzlxz---"
    "bbxbbxbbbbx=bb=x==bbbbxx=",
		"bbbbx==bxxx=bb=xxbbxbb=bb",
		"xxbbbx====xxxbbbbbb=x=xbb",
		"bxb=bxb=bxb=bxb=bxb=bxb=b",
		"bbb=bbbxbbb=bbbxbbb=bbbxb",
		"bbbbbbbbbbbbbbbbbbbbbbbbb"
	],
	50, 50, 50, 100)
}

function loadLevelTwo() {
	org = new Tiles([
		"=b=xxxxb x--=--x-=-=-x-=xxx=---=---=xx   -z=x-z--x--x-=z-x- --x--x-x-l",
		"=b=bbbbx x--xx--=--=----x----==- e---x=   z z--z-x--z -===-x --lxl----x",
		"=x=bbb=b   -x--e---x--x-=e-exxx--  = xx    -=--zx-- -xx-xxx- --lxxxxzlx",
		"=x=xxxx  -=--x--x-x-= -=-xx--=-- = -x   -z== z-x-x---xx-z- x-lxx--x--",
		"=x=xbbtxl-x--x--=--x--x--=e==--e---x--   x-zz xx--=-x--x- l--x-x-ll=",
		"=x=bbbxxxtz=e---------------------=---=   zz xxx-=xxzzx-xx-x xxxzlxz---"
	],
	50, 50, 50, 100)
}


function gotoLevel(person, level) {
	if (level.level == 1) {
		loadLevelOne()
	} else if (level.level == 2) {
		loadLevelTwo()
	}
	levelPortals.remove()
	isMenuScreen = false;
}

function drawMenu() {
	text('Enter a level portal', 100, 100)
	text('1', 100, 400)
	text('2', 200, 400)
	if (kb.pressed(1)) {
		loadLevelOne();
		isMenuScreen = false;
	}
	player.overlaps(levelPortals, gotoLevel)
}

function draw() {
	clear();
	camera.on();
	
	if (isMenuScreen) {
		drawMenu();
//		return;
	}
	
	player.overlaps(coins, collect)
	
	bFloor.collider = "static"
	
	if (player.vel.y < 0) {
		bFloor.collider = "none"
	}
	if (player.vel.y > -1 || player.vel.y == 0) {
		bFloor.collider = "static"
	}
  if (kb.pressed("down") && player.colliding(bFloor)) {
		player.y += 30
	}
	
	if ((player.colliding(bricks) || player.colliding(walls) || player.overlapping(rope) || player.colliding(bFloor)) && kb.presses("up")) {
		player.vel.y = -6.5
	}
	if (player.colliding(trampo) && kb.pressed("up")) {
		player.vel.y = -10
	}
	if (kb.pressing("left")) {
		player.x -= 2
	}
	if (kb.pressing("right")) {
		player.x += 2
	}
	
	if (player.collides(spikes)) {
		player.remove();
	}
	if (player.collides(enemy)) {
		player.remove();
	}
	
	camera.x = player.x
	camera.y = player.y

	allSprites.draw()
	
	camera.off()
	textSize(33)
	text("Score is " + score, 10, 30);
	camera.on();
}
function collect(person, money) {
	if (player.overlapping(coins)) {
		money.remove();
		score += 1
	}
}
async function move(enemies) {
	for (const enemy of enemies) {
		if (player.x > enemy.x) {
			enemy.vel.x = 3
		}
		if (player.x < enemy.x) {
			enemy.vel.x = -3
		}
		if (player.y < enemy.y) {
			enemy.vel.y = - 6.5
		}
	}
	await delay(1000)
	move(enemies)
}