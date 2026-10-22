// =========================================================================
// LG webOS TV & Remote Model Detection & Universal Game Controller Adapter
// =========================================================================

class TVRemoteAdapter {
    constructor() {
        this.tvModel = "LG Smart TV (webOS)";
        this.remoteType = "MAGIC_REMOTE";
        this.remoteName = "LG Magic Remote (MR24 / ג'יירו פעיל)";
        this.hasPointer = false;
        this.isVirtualCursorActive = false;
        this.virtualCursor = { x: 960, y: 540, vx: 0, vy: 0, isDown: false, speed: 18 };

        this.initDeviceDetection();
        this.initInputTracking();
    }

    initDeviceDetection() {
        try {
            if (window.webOSSystem && window.webOSSystem.deviceInfo) {
                const info = JSON.parse(window.webOSSystem.deviceInfo);
                if (info.modelName) {
                    this.tvModel = `LG ${info.modelName}`;
                    if (info.modelName.includes("OLED")) {
                        this.tvModel += " (OLED 4K)";
                    }
                }
            } else if (navigator.userAgent.includes("Web0S")) {
                const match = navigator.userAgent.match(/Web0S[; ]([^;)]+)/);
                this.tvModel = match ? `LG webOS TV (${match[1]})` : "LG webOS Smart TV";
            } else {
                this.tvModel = "דפדפן אינטרנט / TV Browser";
            }
        } catch (e) {
            this.tvModel = "LG Smart TV";
        }

        if (this.tvModel.includes("OLED") || this.tvModel.includes("QNED")) {
            this.remoteType = "MAGIC_REMOTE";
            this.remoteName = "LG Magic Remote (MR24GN / ג'יירו)";
        } else {
            this.remoteType = "MAGIC_REMOTE";
            this.remoteName = "LG Magic Remote (משולב)";
        }

        window.addEventListener("gamepadconnected", (e) => {
            this.remoteType = "GAMEPAD";
            this.remoteName = `שלט גיימינג (${e.gamepad.id.split("(")[0].trim()})`;
            this.updateHUD();
        });
    }

    initInputTracking() {
        let pointerMoved = false;

        window.addEventListener("mousemove", (e) => {
            if (e.movementX !== 0 || e.movementY !== 0) {
                if (!pointerMoved) {
                    pointerMoved = true;
                    this.hasPointer = true;
                    this.remoteType = "MAGIC_REMOTE";
                    this.remoteName = "LG Magic Remote (MR24 סמן ג'יירו פעיל)";
                    this.updateHUD();
                }
            }
        });

        document.addEventListener("cursorStateChange", (e) => {
            if (e.detail && e.detail.visibility) {
                this.hasPointer = true;
                this.remoteType = "MAGIC_REMOTE";
                this.remoteName = "LG Magic Remote (סמן ג'יירו גלוי)";
                this.updateHUD();
            }
        });

        window.addEventListener("keydown", (e) => {
            if ([37, 38, 39, 40].includes(e.keyCode)) {
                if (!this.hasPointer && this.remoteType !== "GAMEPAD") {
                    this.remoteType = "STANDARD_IR";
                    this.remoteName = "שלט LG קלאסי (D-Pad מקשים)";
                    this.updateHUD();
                }
            }
        });
    }

    updateHUD() {
        const tvBadge = document.getElementById("hud-tv-model");
        const remoteBadge = document.getElementById("hud-remote-model");
        if (tvBadge) tvBadge.innerText = this.tvModel;
        if (remoteBadge) remoteBadge.innerText = `🎮 ${this.remoteName}`;
    }
}

window.tvRemoteAdapter = new TVRemoteAdapter();
