// =========================================================================
// LG webOS TV & Remote Model Detection & Universal Game Controller Adapter
// Compatible with: webOS 3.0 through webOS 25 (Chromium / Blink)
// Models: LG OLED (C, G, B series), QNED, NanoCell, UHD TV
// Remotes: Magic Remote (MR24/23/22/21/20), Standard IR Remote (AKB), Gamepad
// =========================================================================

class TVRemoteAdapter {
    constructor() {
        this.tvModel = "LG Smart TV (webOS)";
        this.remoteType = "MAGIC_REMOTE"; // MAGIC_REMOTE, STANDARD_IR, GAMEPAD
        this.remoteName = "LG Magic Remote (MR24 / ג'יירו פעיל)";
        this.hasPointer = false;
        this.isVirtualCursorActive = false;
        this.virtualCursor = { x: 960, y: 540, vx: 0, vy: 0, isDown: false, speed: 18 };
        this.listeners = [];

        this.initDeviceDetection();
        this.initInputTracking();
    }

    initDeviceDetection() {
        // 1. Detect TV Model
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
            }
        } catch (e) {
            this.tvModel = "LG Smart TV";
        }

        // 2. Default Remote heuristic based on LG TV model
        if (this.tvModel.includes("OLED") || this.tvModel.includes("QNED")) {
            this.remoteType = "MAGIC_REMOTE";
            this.remoteName = "LG Magic Remote (MR24GN / ג'יירו)";
        } else {
            this.remoteType = "MAGIC_REMOTE";
            this.remoteName = "LG Magic Remote (משולב)";
        }

        // 3. Gamepad detection
        window.addEventListener("gamepadconnected", (e) => {
            this.remoteType = "GAMEPAD";
            this.remoteName = `שלט גיימינג (${e.gamepad.id.split("(")[0].trim()})`;
            this.updateHUD();
        });
    }

    initInputTracking() {
        // Detect Magic Remote Pointer vs D-Pad
        let pointerMoved = false;

        window.addEventListener("mousemove", (e) => {
            if (e.movementX !== 0 || e.movementY !== 0) {
                if (!pointerMoved) {
                    pointerMoved = true;
                    this.hasPointer = true;
                    this.remoteType = "MAGIC_REMOTE";
                    this.remoteName = "LG Magic Remote (MR24 סמן ג'יירו פעיל)";
                    this.disableVirtualCursor();
                    this.updateHUD();
                }
            }
        });

        // webOS specific cursor visibility event
        document.addEventListener("cursorStateChange", (e) => {
            if (e.detail && e.detail.visibility) {
                this.hasPointer = true;
                this.remoteType = "MAGIC_REMOTE";
                this.remoteName = "LG Magic Remote (סמן ג'יירו גלוי)";
                this.disableVirtualCursor();
                this.updateHUD();
            }
        });

        // If user only presses D-Pad keys without pointer for a while, identify as Standard/D-Pad mode
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

    // Smart Virtual Crosshair for pointer games played with standard IR remote
    enableVirtualCursor(targetIframe) {
        if (this.hasPointer) return; // User has real Magic Remote pointer
        this.isVirtualCursorActive = true;
        
        let cursorEl = document.getElementById("virtual-crosshair");
        if (!cursorEl) {
            cursorEl = document.createElement("div");
            cursorEl.id = "virtual-crosshair";
            cursorEl.style.cssText = `
                position: absolute; width: 36px; height: 36px; pointer-events: none; z-index: 99999;
                border: 3px solid #facc15; border-radius: 50%; box-shadow: 0 0 15px rgba(250,204,21,0.8);
                transform: translate(-50%, -50%); transition: transform 0.05s ease;
            `;
            cursorEl.innerHTML = '<div style="position:absolute;top:50%;left:50%;width:6px;height:6px;background:#ef4444;border-radius:50%;transform:translate(-50%,-50%);"></div>';
            document.body.appendChild(cursorEl);
        }
        cursorEl.style.display = "block";
        cursorEl.style.left = `${this.virtualCursor.x}px`;
        cursorEl.style.top = `${this.virtualCursor.y}px`;
    }

    disableVirtualCursor() {
        this.isVirtualCursorActive = false;
        const cursorEl = document.getElementById("virtual-crosshair");
        if (cursorEl) cursorEl.style.display = "none";
    }

    // Unified key handler for iframe games
    handleGameInput(e, gameIframe) {
        // Color keys shortcuts
        if (e.keyCode === 403) { // Red Button -> Turbo / Secondary Action
            this.dispatchKeyEvent(gameIframe, 88); // 'X' key
            e.preventDefault();
        } else if (e.keyCode === 404) { // Green Button -> Pause
            this.dispatchKeyEvent(gameIframe, 80); // 'P' key
            e.preventDefault();
        } else if (e.keyCode === 405) { // Yellow Button -> Save State / Restart
            this.dispatchKeyEvent(gameIframe, 82); // 'R' key
            e.preventDefault();
        }
    }

    dispatchKeyEvent(iframe, code) {
        try {
            if (iframe && iframe.contentWindow) {
                const evtDown = new KeyboardEvent('keydown', { keyCode: code, which: code, bubbles: true });
                iframe.contentWindow.dispatchEvent(evtDown);
                setTimeout(() => {
                    const evtUp = new KeyboardEvent('keyup', { keyCode: code, which: code, bubbles: true });
                    iframe.contentWindow.dispatchEvent(evtUp);
                }, 100);
            }
        } catch (err) {}
    }
}

window.tvRemoteAdapter = new TVRemoteAdapter();
